from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('risk_register/', include('Risk_register.urls')),
]
