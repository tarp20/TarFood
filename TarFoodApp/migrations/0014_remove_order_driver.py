# Generated by Django 3.0.8 on 2020-07-30 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TarFoodApp', '0013_auto_20200729_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='driver',
        ),
    ]
