from django.db import models


# Create your models here.
class Seller(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, db_index=True)
    cnpj = models.BigIntegerField()
    mail = models.CharField(max_length=50, db_index=True)
    address = models.TextField(blank=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated =  models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.id} - {self.name} - {self.cnpj} - {self.mail} - {self.address} - {self.data_created} - {self.data_updated}"