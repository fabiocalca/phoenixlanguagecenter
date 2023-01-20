from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('bem_vindo',login_required(views.bem_vindo),name='bem_vindo'),
]