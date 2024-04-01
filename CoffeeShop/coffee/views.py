from django.shortcuts import render
from django.http import HttpResponse
from .models import coffee

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def menu(request):
    Coffee = coffee.objects.all()
    return render(request, 'menu.html', {'Coffee' : Coffee})
