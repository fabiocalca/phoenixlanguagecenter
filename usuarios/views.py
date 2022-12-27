from django.shortcuts import render
from django.urls import reverse
from .models import Usuario
from django.views.generic.edit import CreateView
# Create your views here.

def bem_vindo(request):
    context = {}
    return render(request, 'usuarios/bem_vindo.html', context)