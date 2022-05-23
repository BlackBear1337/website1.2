from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Post


class MyTestCase(TestCase):

    def setUp(self):
        Post.objects.all().delete
        self.c = Client

    def test_check_view(self):
        response = self.c.get(reverse('demo:index'))
        self.assertEqual(200, response.status_code)
