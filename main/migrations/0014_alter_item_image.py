# Generated by Django 4.2.5 on 2023-10-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_item_amount_alter_item_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='main/media/albums/'),
        ),
    ]
