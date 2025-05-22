from django.shortcuts import render

# Create your views here.
from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from utilisateurs.models import Client, Utilisateur
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm
@login_required
def utilisateur(request):
    template = loader.get_template('utilisateurs/utilisateurs.html')
    return HttpResponse(template.render(request=request))

def login_page(request):
    template = loader.get_template('utilisateurs/login.html')
    return HttpResponse(template.render(request=request))

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def authentification(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('login')
    return redirect('login')

def deconnexion(request):
    logout(request)
    return redirect('login')

@login_required
def creer_utilisateur(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        photo = request.FILES.get('photo')
        user = Utilisateur.objects.create_user(username=username, password=password, role=role, photo=photo)
        messages.success(request, 'Utilisateur créé avec succès')
        return redirect('utilisateurs')
    else:
        template = loader.get_template('utilisateurs/creer_utilisateur.html')
        context = {}
        return HttpResponse(template.render(context, request=request))



class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')