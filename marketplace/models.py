from django.db import models


# Create your models here.
class Marketplaces(models.Model):

    __tablename__ = 'Marketplaces'

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=300)


class MarketplaceData(models.Model):

    api_address = models.CharField(max_length=200)
    key_security = models.UUIDField()
    endpoints = models.CharField(max_length=100)
