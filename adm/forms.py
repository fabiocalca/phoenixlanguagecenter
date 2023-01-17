from django import forms
from django.forms import ModelForm
from .models import Curso, Professor, Idioma
class CursoCreateForm(ModelForm):
    class Meta:
       model = Curso
       fields = ['curso', 'ativo', 'idioma_do_curso', 'professor_do_curso', 'alunos_do_curso']
    idioma_do_curso = forms.ModelChoiceField(queryset=Idioma.objects.all().order_by('idioma'))
    professor_do_curso = forms.ModelChoiceField(queryset=Professor.objects.all().order_by('usuario_professor__first_name', 'usuario_professor__last_name'))