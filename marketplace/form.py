from django.forms import ModelForm
from marketplace.models import Marketplaces
from marketplace.models import MarketplaceData


class MarketPlaceData(ModelForm):
    class Meta:
        model = MarketplaceData
        fields = ['api_address', 'key_security', 'endpoints']


class MarketplaceForm(ModelForm):
    class Meta:
        model = Marketplaces
        fields = ['name', 'url', 'description']
