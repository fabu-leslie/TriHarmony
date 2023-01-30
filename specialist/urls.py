from django.urls import path
from . import views

app_name = 'specialist'

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),  # specialist dash
    path('add_client/', views.add_client, name='add_client'),
    path('client_detail/<int:client_id>/',
         views.client_detail, name='client_detail'),
    path('parent_data_form/<int:client_id>/',
         views.parent_detail, name='parent_data_form'),
    path('client/<int:client_id>/edit_target_behaviors/',
         views.edit_target_behaviors, name='edit_target_behaviors'),
    path('client/<int:client_id>/add_behavior/',
         views.add_behavior, name='add_behavior'),
]
