from django.urls import path, include
from . import views
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('equipe/', views.EquipeListView.as_view(), name='equipe'),
    path('add_equipe/', staff_member_required(views.EquipeCreateView.as_view()), name='add_equipe'),
    path('<pk>/update_equipe', staff_member_required(views.EquipeUpdateView.as_view()), name='update_equipe'),
    path('<pk>/delete_equipe', staff_member_required(views.EquipeDeleteView.as_view()), name='delete_equipe'),
    path('contact/', views.contactView, name='contact'),
]