from django.contrib import admin
from django.urls import path, include
from seller import views

urlpatterns = [
    path('', include('seller.urls')),
    path('admin/', admin.site.urls),
]
