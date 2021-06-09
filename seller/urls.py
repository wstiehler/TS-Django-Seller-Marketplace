from django.urls import path
from seller import views

urlpatterns = [
    path('seller/', views.seller, name='seller'),
    path('seller_form/', views.seller_form,name='seller_form'),
    path('create_seller/', views.create_seller, name='create_seller'),
    path('view_seller/<int:pk>/', views.view_seller, name='view_seller'),
    path('edit_seller/<int:pk>/', views.edit_seller, name='edit_seller'),
    path('update_seller/<int:pk>/', views.update_seller, name='update_seller'),
    path('delete_seller/<int:pk>/', views.delete_seller, name='delete_seller')
]
