from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError


def validate_amount(value):
    if value <= 0:
        raise ValidationError('Hanya Menerima Jumlah Bulat Positif!')
        
def validate_rating(value):
    if value < 0 or value > 10:
        raise ValidationError('Hanya Menerima Rating dalam skala 0-10!')

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    amount = models.IntegerField(validators=[validate_amount], default=1)
    date_added = models.DateField(auto_now_add=True)
    rating = models.FloatField(validators=[validate_rating], default=0.0)
    description = models.TextField()

    