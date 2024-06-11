from django import forms
from .models import Risk

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['date_raised', 'description', 'likelihood', 'impact', 'owner', 'email', 'mitigating_action']
        widgets = {
            'date_raised': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'likelihood': forms.Select(choices=Risk.LIKELIHOOD_CHOICES),
            'impact': forms.Select(choices=Risk.IMPACT_CHOICES),
            'owner': forms.TextInput(attrs={'size': 30}),
            'email': forms.EmailInput(attrs={'placeholder': 'owner@example.com', 'size': 30}),
            'mitigating_action': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

