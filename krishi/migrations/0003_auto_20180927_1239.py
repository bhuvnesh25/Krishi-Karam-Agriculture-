# Generated by Django 2.1 on 2018-09-27 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krishi', '0002_auto_20180927_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
    ]
