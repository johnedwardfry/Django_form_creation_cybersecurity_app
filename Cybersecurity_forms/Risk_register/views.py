from django.shortcuts import render
from .forms import RiskForm

def risk_register(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RiskForm()
    return render(request, 'index.html', {'form': form})