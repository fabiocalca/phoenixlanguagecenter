from django.shortcuts import render
from django.views.generic.list import ListView
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