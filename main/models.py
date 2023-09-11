from django.db import models
from django.forms import ValidationError


def validate_amount(value):
    if value < 0:
        raise ValidationError('Hanya Menerima Jumlah NonNegatif')
        
def validate_price(value):
    if value % 1000 != 0 or value <= 0:
        raise ValidationError('Hanya Menerima Harga Kelipatan 1000!')

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(validators=[validate_amount])
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(validators=[validate_price])
    description = models.TextField()

    