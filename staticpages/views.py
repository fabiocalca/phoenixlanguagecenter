from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Equipe
# Create your views here.
def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)

def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)

class EquipeListView(ListView):
    model = Equipe
    template_name = 'staticpages/equipe.html'
    context_object_name = 'membros_list'
    
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'ordem')
        return ordering

class EquipeCreateView(CreateView):
    model = Equipe
    fields = ['nome', 'cargo', 'imagem_url', 'descricao', 'ordem']
    def get_success_url(self):
        return reverse('equipe')

class EquipeUpdateView(UpdateView):
    model = Equipe
    fields = ['nome', 'cargo', 'imagem_url', 'descricao', 'ordem']
    success_url = '/equipe/'

class EquipeDeleteView(DeleteView):
    model = Equipe
    success_url = '/equipe/'
