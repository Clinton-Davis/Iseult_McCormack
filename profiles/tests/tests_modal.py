from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from profiles.models import UserProfile


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
        userprofile = UserProfile.objects.get(id=1)
        userprofile.first_name = "Clinton"
        userprofile.last_name = "Davis"
        userprofile.phone_number = "777-8888"
        userprofile.street_address1 = "Street Name"
        userprofile.street_address2 = "Sreet Name2"
        userprofile.town_or_city = "City"
        userprofile.postcode = "Yes"
        userprofile.county = "place"
        userprofile.country = "IE"
        userprofile.save()
        self.userprofile = userprofile

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        user_a = User.objects.get(username="Admin")
        self.assertTrue(user_a.check_password(self.user_a_pw))

    # Test UserProfile is created when User is created
    def test_userprofile(self):
        userprofile = UserProfile.objects.all().count()
        self.assertEqual(userprofile, 1)
        self.assertNotEqual(userprofile, 0)

    def test_profiles(self):
        user_a = User.objects.get(id=1)
        userprofile = UserProfile.objects.get(id=1)
        # Test to see if we have the right profiles
        self.assertEqual(str(userprofile.user), str(user_a.username))

    def test_adding_address(self):
        user_a = User.objects.get(id=1)
        userprofile = UserProfile.objects.get(id=1)
        self.assertEqual(userprofile.first_name, "Clinton")
        self.assertEqual(userprofile.last_name, "Davis")
        self.assertEqual(userprofile.street_address1, "Street Name")
        self.assertEqual(userprofile.town_or_city, "City")
        self.assertEqual(userprofile.postcode, "Yes")
        self.assertEqual(userprofile.country, "IE")

    # Test to see if We can add names to User
    def test_adding_name_to_user(self):
        user_a = User.objects.get(id=1)
        userprofile = UserProfile.objects.get(id=1)
        user_a.first_name = userprofile.first_name
        user_a.last_name = userprofile.last_name
        user_a.save()
        self.assertEqual(user_a.first_name, "Clinton")
        self.assertEqual(user_a.last_name, "Davis")
