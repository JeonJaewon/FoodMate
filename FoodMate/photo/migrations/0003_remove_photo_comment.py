# Generated by Django 3.1 on 2020-08-19 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20200816_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='comment',
        ),
    ]
