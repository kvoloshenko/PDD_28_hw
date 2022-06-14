from django.core.management.base import BaseCommand, CommandError
from blogapp.models import Hh_Response, Hh_Request

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Выбираем ВСЕ Requests
        print('---Выбираем ВСЕ Requests---')
        requests = Hh_Request.objects.all()
        print(type(requests), f'requests = {requests}')
        for request in requests:
            print(type(request), f'request={request} keywords={request.keywords}')
        print('---End---')

        # Выбрать ОДИН Request
        print('---Выбрать ОДИН Request---')
        request = Hh_Request.objects.get(keywords = 'NAME:(java)')
        print(type(request), f'request={request} keywords={request.keywords}')
        print('---End---')

        # Выбрать последний Request
        print('---Выбрать последний Request---')
        last_request = Hh_Request.objects.last()
        print(type(last_request), f'last_request={last_request} keywords={last_request.keywords}')
        print('---End---')

        # Связанные поля
        # ForeignKey
        print('---Выбрать Responses для последнего Request---')
        print(type(last_request), f'last_request={last_request} keywords={last_request.keywords}')
        responses = Hh_Response.objects.filter(request = last_request )
        for response in responses:
            print(type(response), f'response={response} skill_name={response.skill_name}')
        print('---End---')

        # Создание
        Hh_Request.objects.create(keywords = 'NAME:(Python) and (AI OR ML)')
        last_request = Hh_Request.objects.last()
        Hh_Response.objects.create(request = last_request, skill_name = 'python', skill_count = 18, skill_persent = 25)
        Hh_Response.objects.create(request=last_request, skill_name='django', skill_count=7, skill_persent=10)
        Hh_Response.objects.create(request=last_request, skill_name='postgresql', skill_count=4, skill_persent=6)