from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse
from django.http import HttpResponse
from .models import Usuario
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.

def bem_vindo(request):
    context = {}
    return render(request, 'usuarios/bem_vindo.html', context)
