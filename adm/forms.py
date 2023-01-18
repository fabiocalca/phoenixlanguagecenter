from django import forms
from django.forms import ModelForm
from usuarios.models import Empresa, Aluno
from .models import Curso, Professor, Idioma, Pagamento
from usuarios.models import Usuario
class CursoCreateForm(ModelForm):
    class Meta:
       model = Curso
       fields = ['curso', 'ativo', 'idioma_do_curso', 'professor_do_curso', 'alunos_do_curso']
    idioma_do_curso = forms.ModelChoiceField(queryset=Idioma.objects.all().order_by('idioma'))
    professor_do_curso = forms.ModelChoiceField(queryset=Professor.objects.all().order_by('usuario_professor__first_name', 'usuario_professor__last_name'))

class PagamentoCreateForm(ModelForm):
   class Meta:
      model = Pagamento
      fields = ['curso','valor', 'pago', 'aulas_no_pacote']
   curso = forms.ModelChoiceField(queryset=Curso.objects.all().order_by('curso'))
class IdiomaCreateForm(ModelForm):
   class Meta:
      model = Idioma
      fields = ['idioma']

class UsuarioCreateForm(ModelForm):
   class Meta:
      model = Usuario
      fields = ['first_name', 'last_name', 'username', 'password', 'email', 'telefone','data_de_nascimento', 'telefone', 'eh_aluno','eh_professor','eh_empresa']

class EmpresaCreateForm(ModelForm):
   class Meta:
      model = Empresa
      fields = ['usuario_empresa', 'nome', 'contrato_ativo']
   usuario_empresa = forms.ModelChoiceField(queryset=Usuario.objects.all().order_by('username'))

class ProfessorCreateForm(ModelForm):
   class Meta:
      model = Professor
      fields = ['usuario_professor', 'ativo']
   usuario_professor = forms.ModelChoiceField(queryset=Usuario.objects.all().order_by('username'))

class AlunoCreateForm(ModelForm):
   class Meta:
      model = Aluno
      fields = ['usuario_aluno', 'empresa_vinculada']
   usuario_aluno = forms.ModelChoiceField(queryset=Usuario.objects.all().order_by('username'))
   empresa_vinculada = forms.ModelChoiceField(queryset=Empresa.objects.all().order_by('nome'))
      