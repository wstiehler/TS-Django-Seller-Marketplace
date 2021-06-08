from django.db import models
from django.forms import ModelForm
from marketplace.models import Marketplaces

class MarketplaceForm(ModelForm):
    class Meta:
        model = Marketplaces
        fields = ['name', 'url', 'description']

