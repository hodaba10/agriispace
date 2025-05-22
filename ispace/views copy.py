from django.contrib import messages  # ✅ BON !

from unittest import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template import loader
from ispace.forms import BatimentForm
from ispace.models import Bande, Batiment, Materiel
# Create your views here.
# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'ispace/dashbord.html')

@login_required
def batiment(request):
    batiments = Batiment.objects.all()
    context= {
        'batiments':batiments,} 
    template = loader.get_template('ispace/batiments.html')
    return HttpResponse(template.render(context ,  request))

"""ajout d'une batiments"""
@login_required
def add_batiment(request):
    if request.method == 'POST':
        code = request.POST['code']
        designation = request.POST['designation']
        capacite = request.POST['capacite']
        dimensions = request.POST['dimensions'] or "N/A"
        type_batiment = request.POST['type']

        if Batiment.objects.filter(code=code).exists():
            messages.error(request, 'Un bâtiment avec ce code existe déjà.')
            return redirect('batiment')

        try:
            Batiment.objects.create(
                code=code,
                designation=designation,
                capacite=capacite,
                dimensions=dimensions,
                type=type_batiment
            )
            messages.success(request, 'Bâtiment ajouté avec succès.')
        except Exception as e:
            messages.error(request, f'Erreur : {e}')
        return redirect('batiment')
    return redirect('batiment')


"""suppression de batiment"""
@login_required
def delete_batiment(request , batiment_id):
        batiment = get_object_or_404(Batiment, id=batiment_id)

        try:
            batiment.delete()
            messages.success(request, 'batiment supprimée avec succés')
            return redirect('batiment')
        except:
            messages.error(request, 'Une erreure s\est produite')

        return redirect('batiment')   

"""modification de batiment"""
@login_required
def update_batiment(request, batiment_id):
    batiment = get_object_or_404(Batiment, id=batiment_id)

    bandes = Bande.objects.filter(batiment__id=batiment.id)
    materiels = Materiel.objects.filter(batiment__id=batiment.id)

    return render(request, 'ispace/edit_batiment.html', {
        'batiment': batiment,
        'bandes': bandes,
        'materiels': materiels,
    })



from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import TypeBande, Bande, Mortalite, Materiel, CategorieDepense, DepenseAvicole
from .forms import TypeBandeForm, BandeForm, MortaliteForm, MaterielForm, DepenseAvicoleForm

# TypeBande Views
class TypeBandeListView(ListView):
    model = TypeBande
    template_name = 'type_bande_list.html'
    context_object_name = 'types'

class TypeBandeCreateView(CreateView):
    model = TypeBande
    form_class = TypeBandeForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('type_bande_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Type de Bande"
        context['cancel_url'] = reverse_lazy('type_bande_list')
        return context

class TypeBandeUpdateView(UpdateView):
    model = TypeBande
    form_class = TypeBandeForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('type_bande_list')

class TypeBandeDeleteView(DeleteView):
    model = TypeBande
    success_url = reverse_lazy('type_bande_list')
    template_name = 'ispace/typebande_confirm_delete.html'

# Bande Views
class BandeListView(ListView):
    model = Bande
    template_name = 'bande_list.html'
    context_object_name = 'bandes'
    
    def get_queryset(self):
        return Bande.objects.select_related('batiment', 'type_bande')

class BandeCreateView(CreateView):
    model = Bande
    form_class = BandeForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('bande_list')

class BandeDetailView(DetailView):
    model = Bande
    template_name = 'bande_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mortalites'] = self.object.mortalite_set.all()
        context['depenses'] = self.object.depenseavicole_set.all()
        return context

class BandeUpdateView(UpdateView):
    model = Bande
    form_class = BandeForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('bande_list')
    
class BandeDeleteView(DeleteView):
    model = Bande
    template_name = 'ispace/bande_confirm_delete.html'
    success_url = reverse_lazy('bande_list')    

# Mortalite Views
class MortaliteListView(ListView):
    model = Mortalite
    template_name = 'mortalite_list.html'
    context_object_name = 'mortalites'
    
    def get_queryset(self):
        return Mortalite.objects.select_related('bande')

class MortaliteCreateView(CreateView):
    model = Mortalite
    form_class = MortaliteForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('mortalite_list')

class MortaliteUpdateView(UpdateView):
    model = Mortalite
    form_class = MortaliteForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('mortalite_list')

class MortaliteDeleteView(DeleteView):
    model = Mortalite
    success_url = reverse_lazy('mortalite_list')
    template_name = 'ispace/mortalite_confirm_delete.html'

# Materiel Views
class MaterielListView(ListView):
    model = Materiel
    template_name = 'materiel_list.html'
    context_object_name = 'materiels'
    
    def get_queryset(self):
        return Materiel.objects.select_related('batiment')

class MaterielCreateView(CreateView):
    model = Materiel
    form_class = MaterielForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('materiel_list')

class MaterielUpdateView(UpdateView):
    model = Materiel
    form_class = MaterielForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('materiel_list')

class MaterielDeleteView(DeleteView):
    model = Materiel
    success_url = reverse_lazy('materiel_list')
    template_name = 'confirm_delete.html'

# DepenseAvicole Views
class DepenseAvicoleListView(ListView):
    model = DepenseAvicole
    template_name = 'depense_list.html'
    context_object_name = 'depenses'
    
    def get_queryset(self):
        return DepenseAvicole.objects.select_related('bande', 'categorie')

class DepenseAvicoleCreateView(CreateView):
    model = DepenseAvicole
    form_class = DepenseAvicoleForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('depense_list')

class DepenseAvicoleUpdateView(UpdateView):
    model = DepenseAvicole
    form_class = DepenseAvicoleForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('depense_list')

class DepenseAvicoleDeleteView(DeleteView):
    model = DepenseAvicole
    success_url = reverse_lazy('depense_list')
    template_name = 'ispace/depense_confirm_delete.html'
    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CategorieDepense
from .forms import CategorieDepenseForm

class CategorieDepenseListView(ListView):
    model = CategorieDepense
    template_name = 'ispace/categorie_depense_list.html'
    context_object_name = 'categories'

class CategorieDepenseCreateView(CreateView):
    model = CategorieDepense
    form_class = CategorieDepenseForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('categorie_depense_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nouvelle Catégorie"
        context['cancel_url'] = reverse_lazy('categorie_depense_list')
        return context

class CategorieDepenseUpdateView(UpdateView):
    model = CategorieDepense
    form_class = CategorieDepenseForm
    template_name = 'ispace/generic_form.html'
    success_url = reverse_lazy('categorie_depense_list')

class CategorieDepenseDeleteView(DeleteView):
    model = CategorieDepense
    success_url = reverse_lazy('categorie_depense_list')
    template_name = 'ispace/categorie_confirm_delete.html'    