# Generated by Django 4.2.5 on 2023-09-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_item_price_item_rating_alter_item_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='artist',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]
