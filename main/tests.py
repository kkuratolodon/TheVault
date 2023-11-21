from django.forms import ValidationError
from django.test import Client, TestCase

from main.models import *


class mainTest(TestCase):
    # testing dari tutorial 1
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')
    