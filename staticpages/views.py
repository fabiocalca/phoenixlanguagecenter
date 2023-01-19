from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
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

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["first_name"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["fabiocalcacarvalho@usp.br"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "staticpages/contact.html", {"form": form})

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
