from django.urls import path
from . import views

app_name = 'Risk_register'

urlpatterns = [
    path('', views.risk_register, name='index'),
]