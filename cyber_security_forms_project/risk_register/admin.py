from django.contrib import admin
from django import forms
from .models import Risk
from django.db import models

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('description', 'severity', 'owner', 'date_raised')
    readonly_fields = ('severity',)
    formfield_overrides = {
        models.DateField: {'widget': forms.DateInput(attrs={'type': 'date'})},
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 5, 'cols': 40})},
        models.CharField: {'widget': forms.TextInput(attrs={'size': 40})},
        models.IntegerField: {'widget': forms.Select(choices=Risk.LIKELIHOOD_CHOICES)},
    }

    def severity(self, obj):
        return obj.severity
    severity.short_description = 'Severity'

