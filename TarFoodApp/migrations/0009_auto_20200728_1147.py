# Generated by Django 3.0.8 on 2020-07-28 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TarFoodApp', '0008_auto_20200728_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='adress',
            new_name='address',
        ),
    ]