from django.test import TestCase, Client
from django.urls import reverse


class MyTestCase(TestCase):

    def tests_check_view(self):
        response = self.c.get(reverse('demo:index'))
        self.assertEqual(200, response.status_code)