# from django.test import TestCase, Client, RequestFactory
# from django.urls import reverse
# from .views import (IndexView, aboutview, GalleryView,
#                     TermsView, PrivacyView, ContactView)


# class TestHomeViews(TestCase):

#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_home_view(self):
#         request = self.factory.get('/home/index')
#         response = IndexView.as_view()(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed('home/index.html')

#     def setUp(self):
#         self.client = Client()
#         self.home = reverse("about")

#     def test_about_view(self):
#         response = self.client.get(self.home)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed('home/about.html')
