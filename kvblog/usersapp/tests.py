from django.test import TestCase
from usersapp.models import BlogUser

# Create your tests here.
class BlogUserTestCase(TestCase):
    def setUp(self):
        self.user = BlogUser.objects.create_user(username='test_user',
                                            email='test@test.com',
                                            password='us1234567')
    def test_username(self):
        self.assertEqual(self.user.username,'test_user')