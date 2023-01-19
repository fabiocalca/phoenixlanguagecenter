from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('equipe/', views.EquipeListView.as_view(), name='equipe')
]