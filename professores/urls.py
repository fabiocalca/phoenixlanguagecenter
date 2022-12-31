from django.contrib import admin
from django.urls import path
from . import views
from usuarios.decorators import professor_required
urlpatterns = [
    path('', views.index, name='professor_index'),
    path('create_aula', views.AulaCreateView.as_view(), name='create_aula'),
    path('aulas',views.AulaListView.as_view(), name='aulas'),
    path('<pk>/update_aula', professor_required(views.AulaUpdateView.as_view()), name='update_aula'),
    path('<pk>/delete_aula', professor_required(views.AulaDeleteView.as_view()), name='delete_aula'),
]