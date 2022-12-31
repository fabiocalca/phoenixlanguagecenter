from django.shortcuts import render
from .forms import AulaCreateForm
from .models import Aula
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'professores/index.html', context={})

class AulaCreateView(CreateView):
    template_name = 'professores/create_aula.html'
    form_class = AulaCreateForm

    def get_form_kwargs(self):
        kwargs = super(AulaCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    def get_success_url(self):
        return reverse('aulas')

class AulaListView(ListView):
    model = Aula
    context_object_name = 'aula_list'
    def get_queryset(self):
        return super().get_queryset().filter(professor=self.request.user.professor)

class AulaUpdateView(UpdateView):
    model = Aula
    fields = ['titulo', 'curso', 'presente', 'data']
    success_url = "/professores/aulas"

class AulaDeleteView(DeleteView):
    model = Aula
    success_url = "/professores/aulas"
    template_name = "professores/aula_delete_confirm.html"

class AulaDetailView(DetailView):
    model = Aula