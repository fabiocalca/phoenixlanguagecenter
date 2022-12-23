from django.forms import ModelForm
from .models import Aula
from adm.models import Curso
from usuarios.models import Professor
class AulaCreateForm(ModelForm):
    class Meta:
       model = Aula
       fields = ['titulo', 'curso', 'professor', 'presente', 'data']
    
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(AulaCreateForm, self).__init__(*args, **kwargs)
       self.fields['curso'].queryset = Curso.objects.filter(professor_do_curso=user.professor)
       self.fields['professor'].queryset = Professor.objects.filter(id=user.professor.id)