# Generated by Django 4.1.1 on 2022-09-26 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='no_of_pages',
        ),
    ]
