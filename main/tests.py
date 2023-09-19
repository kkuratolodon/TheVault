from django.forms import ValidationError
from django.test import Client, TestCase

from main.models import *


class mainTest(TestCase):
    # testing dari tutorial 1
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    # testing apakah model Item menerima nama, yang valid
    def test_valid_name(self):
        item = Item(name="Valid Name", artist = "Valid", amount=13, rating = 6.9, description="Desription")
        item.full_clean()
        self.assertTrue(item)

        item = Item(name="", artist = "Valid", amount=13, rating = 6.9, description="Desription")
        with self.assertRaises(ValidationError):
            item.full_clean()
    
    # testing apakah model Item menerima jumlah yang valid
    def test_valid_amount(self):
        # jumlah hanya boleh integer >= 1
        item = Item(name="Valid Name", artist = "Valid", amount=1, rating = 6.9, description="Description")
        item.full_clean()
        with self.assertRaises(ValidationError):
            item = Item(name="Valid Name", artist = "Valid", amount=13.2, rating = 6.9, description="Description")
            item.full_clean()
            item = Item(name="Valid Name", artist = "Valid", amount=-5, rating = 6.9, description="Description")
            item.full_clean()

    # testing apakah model Item menerima rating yang valid
    def test_valid_rating(self):
        # rating hanya menerima float dari 0 - 10 (inklusif)
        item = Item(name="Valid Name", artist = "Valid", amount=12, rating = 6.9, description="Description")
        item.full_clean()
        with self.assertRaises(ValidationError):
            item = Item(name="Valid Name", artist = "Valid", amount=12, rating = 69, description="Description")
            item.full_clean()
            item = Item(name="Valid Name", artist = "Valid", amount=12, rating = -69, description="Description")
            item.full_clean()