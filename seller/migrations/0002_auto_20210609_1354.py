# Generated by Django 3.2.4 on 2021-06-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='data_created',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='data_updated',
        ),
    ]