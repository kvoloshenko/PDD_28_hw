from django.core.management.base import BaseCommand, CommandError
from blogapp.models import Hh_Response, Hh_Request
import hhru.all_data as ad
import pprint

class Command(BaseCommand):

    def handle(self, *args, **options):
        print ('---Run fill_db_parser---')
        skeys = 'NAME:(C#)'
        ad.set_keywords(skeys)
        result = ad.get_data(skeys)
        # print(type(result))
        # print(type(result[0]['requirements']))
        pprint.pprint(result)
        keywords = result[0]['keywords']
        # print(f'keywords={keywords}')
        Hh_Request.objects.create(keywords = keywords)
        last_request = Hh_Request.objects.last()

        requirements_l = result[0]['requirements']
        # print(type(requirements_l), f'requirements_l={requirements_l}')
        for item in requirements_l:
            # print(f'item={item}')
            # print(f'{item["name"]} {item["count"]} {round(int(item["persent"]))}')
            Hh_Response.objects.create(request=last_request, skill_name=item["name"], skill_count=item["count"], skill_persent=round(int(item["persent"])))

