from django.urls import path
from . import views

app_name = 'risk_register'

urlpatterns = [
    path('', views.index, name='index'),
    path('risk_delete/<int:id>/', views.risk_delete, name='risk_delete'),
    path('export_risks_to_pdf/', views.export_risks_to_pdf, name='export_risks_to_pdf'),
]
