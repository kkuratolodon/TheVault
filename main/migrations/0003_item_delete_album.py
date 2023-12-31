# Generated by Django 4.2.5 on 2023-09-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_product_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
