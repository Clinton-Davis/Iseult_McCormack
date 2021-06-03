from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase


class UserTest(TestCase):
    
    def setUp(self):
        user_a = User(username='Admin', email='admin@admin.com')
        user_a_pw = '12345'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
    
    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
    
    def test_user_password(self):
        user_a = User.objects.get(username="Admin")
        self.assertTrue(user_a.check_password(self.user_a_pw))
    
    # def test_login_url(self):
    #     login_url = settings.LOGIN_URL
    #     # responce = self.client.post(url, {}, follow=True)
    #     data = {"username" : "Admin", "password" : self.user_a_pw}
    #     response = self.client.post(login_url, data, follow=True)
    #     status_code = response.status_code
    #     redirect_path = response.request.get("PATH_INFO")
    #     print(redirect_path)
    #     # self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
    #     self.assertEqual(status_code, 200)
        
        