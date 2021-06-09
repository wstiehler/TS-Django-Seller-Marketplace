from django import urls
from django.contrib import admin
from django.urls import path, include
from marketplace import views
from marketplace.views import marketplaces, marketplacesForm, createMarketplaces, editMarketplace, updateMarketplace, deleteMarketplace, viewMarketplace

urlpatterns = [
    # path('', include('seller.urls')),
    path('admin/', admin.site.urls),
    # path('seller/', include('seller.urls')),
    path('', include('marketplace.urls'))
]
