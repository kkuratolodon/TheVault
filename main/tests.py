from django.forms import ValidationError
from django.test import Client, TestCase

from .models import *


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
        item = Item(name="Valid Name", amount=13, price = 100000, description="Desc")
        item.full_clean()
        self.assertTrue(item)

        item = Item(name="", amount=13, price = 100000, description="Desc")
        with self.assertRaises(ValidationError):
            item.full_clean()

    # testing apakah model Item menerima jumlah yang valid
    def test_valid_amount(self):
        # jumlah hanya boleh integer >= 0
        item = Item(name="Valid Name", amount=0, price = 10000, description="Description")
        item.full_clean()
        with self.assertRaises(ValidationError):
            item = Item(name="Valid Name", amount=13.2, price = 10000, description="Description")
            item.full_clean()
            item = Item(name="Valid Name", amount=-5, price = 10000, description="Description")
            item.full_clean()

    # testing apakah model Item menerima harga yang valid
    def test_valid_price(self):
        # harga hanya boleh integer >= 0 kelipatan 1000 (asumsi dalam rupiah)
        item = Item(name="Valid Name", amount=12, price = 1000, description="Description")
        item.full_clean()
        with self.assertRaises(ValidationError):
            item = Item(name="Valid Name", amount=12, price = 1000.0, description="Description")
            item.full_clean()
            item = Item(name="Valid Name", amount=12, price = -1000, description="Description")
            item.full_clean()