# Generated by Django 3.2.4 on 2021-06-08 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MarketplaceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_address', models.CharField(max_length=100)),
                ('key_security', models.CharField(max_length=10)),
                ('endpoints', models.CharField(max_length=100)),
                ('marketplace_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.marketplaces')),
            ],
        ),
    ]
