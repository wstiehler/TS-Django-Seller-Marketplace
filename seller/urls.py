from django.urls import path
from seller import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('seller/', views.list_seller, name='seller'),
    path('seller_form/', views.seller_form,name='seller_form'),
    path('create_seller/', views.create_seller, name='create_seller'),
    path('list_seller/<int:id>/', views.list_seller, name='list_seller'),
    path('update_seller/<int:id>/', views.update_seller, name='update_seller'),
    path('delete_seller/<int:id>/', views.delete_seller, name='delete_seller')

]
