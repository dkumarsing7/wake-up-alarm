from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'alarm_theme/templates/alarm_theme/home.html')
