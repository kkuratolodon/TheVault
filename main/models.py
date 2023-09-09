from django.db import models
from django.forms import ValidationError


class Album(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()

    def validate_amount(self):
        if self.amount < 0 or type(self.amount) is not int:
            raise ValidationError('')
        
    def validate_price(self):
        if self.price % 1000 != 0 or self.price <= 0:
            raise ValidationError('')