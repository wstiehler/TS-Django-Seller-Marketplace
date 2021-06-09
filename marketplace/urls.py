from django.urls import path
from marketplace import views

urlpatterns = [
    path('marketplace/', views.marketplaces, name='home-marketplace'),
    path('marketplacesForm/', views.marketplacesForm, name='marketplacesForm'),
    path('createMarketplaces/', views.createMarketplaces, name='createMarketplaces'),
    path('viewMarketplace/<int:pk>/', views.viewMarketplace, name='viewMarketplace'),
    path('editMarketplace/<int:pk>/', views.editMarketplace, name='editMarketplace'),
    path('updateMarketplace/<int:pk>/', views.updateMarketplace, name='updateMarketplace'),
    path('deleteMarketplace/<int:pk>/', views.deleteMarketplace, name='deleteMarketplace'),
]
