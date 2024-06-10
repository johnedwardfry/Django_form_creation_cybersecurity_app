from django.contrib import admin
from .models import Risk

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('date_raised', 'description', 'likelihood', 'impact', 'severity', 'owner', 'email', 'mitigating_action')
