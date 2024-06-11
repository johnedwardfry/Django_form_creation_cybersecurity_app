from django.shortcuts import render
from .models import Risk
from .forms import RiskForm

def index(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RiskForm()

    risks = Risk.objects.all()
    return render(request, 'risk_register/index.html', {'form': form, 'risks': risks})


