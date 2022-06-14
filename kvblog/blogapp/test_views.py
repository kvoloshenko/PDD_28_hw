from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import BlogUser

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_required(self):
        BlogUser.objects.create_user(username='test_user',
                                     email=self.fake.email(),
                                     password='us1234567')
        # Он не вошел
        response = self.client.get('/form/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/history/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/req_list/')
        self.assertEqual(response.status_code, 302)

       # Логиним
        self.client.login(username='test_user', password='us1234567')

        response = self.client.get('/form/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/history/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/req_list/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/req_create/')
        self.assertEqual(response.status_code, 403)

    def test_login_required_dbAdmin(self):
        BlogUser.objects.create_user(username='test_user',
                                         email=self.fake.email(),
                                         password='us1234567',
                                         is_dbAdmin=True)
        # Логиним
        self.client.login(username='test_user', password='us1234567')

        response = self.client.get('/req_create/')
        self.assertEqual(response.status_code, 200)

    def test_logined_dbAdmin(self):
        BlogUser.objects.create_user(username='test_user',
                                         email=self.fake.email(),
                                         password='us1234567',
                                         is_dbAdmin=True)
        # Логиним
        self.client.login(username='test_user', password='us1234567')

        response = self.client.get('/req_create/')
        self.assertEqual(response.status_code, 200)

        # post зарос
        response = self.client.post('/req_create/',
                                    {'keywords': 'Python'})

        self.assertEqual(response.status_code, 302)
