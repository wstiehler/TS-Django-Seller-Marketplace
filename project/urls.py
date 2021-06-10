from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='base'),
    path('', include('seller.urls')),
    path('', include('marketplace.urls')),
    path('admin/', admin.site.urls),
]
