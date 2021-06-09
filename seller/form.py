from django.db import models
from django.forms import ModelForm
from .models import Seller

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'cnpj', 'mail', 'address']