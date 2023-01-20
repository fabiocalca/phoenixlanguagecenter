from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staticpages.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('adm/', include('adm.urls'), name='adm'),
    path('professores/', include('professores.urls'), name='professores'),
    path('alunos/', include('alunos.urls')),
]
