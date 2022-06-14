from django.test import TestCase
from usersapp.models import BlogUser
from .models import Hh_Request, Hh_Response

# Create your tests here.
class Hh_RequestTestCase(TestCase):
    def setUp(self):
        user = BlogUser.objects.create_user(username='test_user',
                                            email='test@test.com',
                                            password='us1234567')
        self.hh_request = Hh_Request.objects.create(keywords='Python',
                                              user=user)
        self.hh_response= Hh_Response.objects.create(request=self.hh_request,
                                   skill_name='test_skill_name',
                                   skill_count=10,
                                   skill_persent=1)
        # print(str(self.hh_response))

    def test_hh_request_str(self):
        self.assertEqual(str(self.hh_request.keywords), 'Python')

    def test_hh_response_str(self):
        self.assertEqual(str(self.hh_response), 'Python test_skill_name 10 1%')

    def test_hh_request_create(self):
        print(self.hh_request.create)
        self.assertIsNotNone(self.hh_request.create)

    def test_hh_request_update(self):
        print(self.hh_request.update)
        self.assertIsNotNone(self.hh_request.update)
