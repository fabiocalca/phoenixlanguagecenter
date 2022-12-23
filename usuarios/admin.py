from django.contrib import admin
from .models import Usuario, Empresa, Aluno, Professor
admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Professor)
admin.site.register(Aluno)