from django.db import models


# Create your models here.
class Seller(models.Model):

    name = models.CharField(max_length=50, db_index=True)
    cnpj = models.CharField(max_length=50, db_index=True)
    mail = models.CharField(max_length=50, db_index=True)
    address = models.CharField(max_length=50, db_index=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated =  models.DateTimeField(auto_now=True)

