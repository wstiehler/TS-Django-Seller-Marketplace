from django.db import models

# Create your models here.
class Marketplaces(models.Model):

    __tablename__ = 'Marketplaces'

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"""{self.name} - {self.url} - {self.description}"""

class MarketplaceData(models.Model):

    __tablename__ = 'MarketplaceData'
    
    marketplace_id = models.ForeignKey(to = Marketplaces, on_delete=models.CASCADE)
    api_address = models.CharField(max_length=100)
    key_security = models.CharField(max_length=10)
    endpoints = models.CharField(max_length=100)
    