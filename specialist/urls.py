from django.urls import path
from . import views

app_name = 'specialist'

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),  # specialist dash
    path('add_client/', views.add_client, name='add_client'),
    path('client_detail/<int:client_id>/',
         views.client_detail, name='client_detail'),
]
