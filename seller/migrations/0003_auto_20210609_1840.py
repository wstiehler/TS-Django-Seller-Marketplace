# Generated by Django 3.2.4 on 2021-06-09 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20210609_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='data_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
