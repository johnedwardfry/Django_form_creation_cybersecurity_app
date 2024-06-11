from django.urls import path
from . import views

app_name = 'risk_register'

urlpatterns = [
    path('', views.index, name='index'),
]
