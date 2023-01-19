from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('equipe/', views.EquipeListView.as_view(), name='equipe'),
    path('add_equipe/', views.EquipeCreateView.as_view(), name='add_equipe'),
    path('<pk>/update_equipe', views.EquipeUpdateView.as_view(), name='update_equipe'),
    path('<pk>/delete_equipe', views.EquipeDeleteView.as_view(), name='delete_equipe'),
]