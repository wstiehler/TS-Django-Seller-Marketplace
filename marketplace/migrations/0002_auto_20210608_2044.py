# Generated by Django 3.2.4 on 2021-06-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplacedata',
            name='api_address',
            field=models.CharField(auto_created=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='marketplacedata',
            name='endpoints',
            field=models.CharField(auto_created=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='marketplacedata',
            name='key_security',
            field=models.CharField(auto_created=True, max_length=10),
        ),
    ]
