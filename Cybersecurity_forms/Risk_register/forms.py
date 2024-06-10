from django import forms
from .models import Risk

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['description', 'likelihood', 'impact', 'owner', 'email', 'mitigating_action']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
            'likelihood': forms.Select(choices=Risk._meta.get_field('likelihood').choices),
            'impact': forms.Select(choices=Risk._meta.get_field('impact').choices),
            'email': forms.EmailInput(attrs={'placeholder': 'owner@example.com'}),
        }
