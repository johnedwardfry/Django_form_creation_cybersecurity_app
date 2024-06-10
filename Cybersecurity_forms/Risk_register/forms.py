from django import forms
from .models import Risk

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['description', 'likelihood', 'impact', 'owner', 'email', 'mitigating_action', 'date_raised']
        widgets = {
            'date_raised': forms.DateInput(attrs={'type': 'date'}),
        }