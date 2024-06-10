from django.shortcuts import render

def index(request):
    return render(request, 'Risk_register/index.html')
