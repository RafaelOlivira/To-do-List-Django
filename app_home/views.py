from django.shortcuts import render
from .models import Usuario
# Create your views here.

def home(request): 
    usuario = Usuario.objects.all()
    return render(request,"./app_home/home.html",{"usuario":usuario}) 
