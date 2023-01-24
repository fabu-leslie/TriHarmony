from django.urls import path
from . import views

app_name = 'specialist'
urlpatterns = [
    path('', views.home, name='home')
]
