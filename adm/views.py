from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Pagamento, Idioma
from professores.models import Aula
from usuarios.models import Usuario, Empresa, Aluno, Professor
from .forms import CursoCreateForm, IdiomaCreateForm, PagamentoCreateForm, ProfessorCreateForm, AlunoCreateForm, UsuarioCreateForm, EmpresaCreateForm
def index(request):
    alunos = Aluno.objects.all().count()
    cursos = Curso.objects.all().count()
    professores = Professor.objects.all().count()
    aulas = Aula.objects.all().count()
    context = {'alunos': alunos,
    'cursos': cursos,
    'professores': professores,
    'aulas': aulas}
    return render(request, 'adm/index.html', context)
class AulaListView(ListView):
    model = Aula
    context_object_name = 'aula_list'
    template_name = "adm/aula_list.html"
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-data')
        return ordering

    def get_queryset(self):
        cursos = self.request.GET.get('nome')
        if cursos:
            qs = Aula.objects.filter(curso__curso__icontains=cursos)
        else:
            qs = Aula.objects.all()
        return qs
    

class AulaDetailView(DetailView):
    model = Aula
    template_name = 'adm/aula_detail.html'

# Cursos
class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoCreateForm
    def get_success_url(self):
        return reverse('cursos')

class CursoListView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_queryset(self):
        cursos = self.request.GET.get('nome')
        if cursos:
            qs = Curso.objects.filter(curso__icontains=cursos)
        else:
            qs = Curso.objects.all()
        return qs

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoCreateForm
    success_url = "/adm/cursos/"

class CursoDeleteView(DeleteView):
  model = Curso
  success_url ="/adm/cursos/"
  template_name = "adm/curso_delete_confirm.html"

# Pagamentos
class PagamentoCreateView(CreateView):
    model = Pagamento
    form_class = PagamentoCreateForm
    def get_success_url(self):
        return reverse('pagamentos')

class PagamentoListView(ListView):
    model = Pagamento
    context_object_name = 'pagamento_list'
    paginate_by=10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PagamentoUpdateView(UpdateView):
    model = Pagamento
    form_class = PagamentoCreateForm
    success_url = "/adm/pagamentos/"

class PagamentoDeleteView(DeleteView):
    model = Pagamento
    success_url ="/adm/pagamentos/"
    template_name = "adm/pagamento_delete_confirm.html"

# Idiomas

class IdiomaListView(ListView):
    model = Idioma
    context_object_name = 'idioma_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class IdiomaCreateView(CreateView):
    model = Idioma
    form_class = IdiomaCreateForm
    def get_success_url(self):
        return reverse('idiomas')

class IdiomaUpdateView(UpdateView):
    model = Idioma
    form_class = IdiomaCreateForm
    success_url = "/adm/idiomas/"

class IdiomaDeleteView(DeleteView):
    model = Idioma
    success_url ="/adm/idiomas/"
    template_name = "adm/idioma_delete_confirm.html"

# Usuarios
class UsuarioListView(ListView):
    model = Usuario
    context_object_name = 'usuario_list'
    
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-first_name')
        return ordering

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioCreateForm
    def get_success_url(self):
        return reverse('adm_index')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioCreateForm
    success_url = "/adm/usuarios/"

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url ="/adm/usuarios/"
    template_name = "adm/usuario_delete_confirm.html"

# Empresas
class EmpresaListView(ListView):
    model = Empresa
    context_object_name = 'empresa_list'

class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaCreateForm
    def get_success_url(self):
        return reverse('adm_index')

class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaCreateForm
    success_url = "/adm/empresas/"

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url ="/adm/empresas/"
    template_name = "adm/empresa_delete_confirm.html"

# Professores
class ProfessorListView(ListView):
    model = Professor
    context_object_name = 'professor_list'

class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorCreateForm
    def get_success_url(self):
        return reverse('adm_index')

class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorCreateForm
    success_url = "/adm/professores/"

class ProfessorDeleteView(DeleteView):
    model = Professor
    success_url ="/adm/professores/"
    template_name = "adm/professor_delete_confirm.html"

# Alunos
class AlunoListView(ListView):
    model = Aluno
    context_object_name = 'aluno_list'

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoCreateForm
    def get_success_url(self):
        return reverse('adm_index')

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoCreateForm
    success_url = "/adm/alunos/"

class AlunoDeleteView(DeleteView):
    model = Aluno
    success_url ="/adm/alunos/"
    template_name = "adm/professor_delete_confirm.html"