from django import forms
from .models import Batiment, TypeBande, Bande

class BatimentForm(forms.ModelForm):
    class Meta:
        model = Batiment
        fields = '__all__'

class TypeBandeForm(forms.ModelForm):
    class Meta:
        model = TypeBande
        fields = '__all__'

class BandeForm(forms.ModelForm):
    class Meta:
        model = Bande
        fields = '__all__'


from django import forms
from .models import TypeBande, Bande, Mortalite, Materiel, DepenseAvicole

class TypeBandeForm(forms.ModelForm):
    class Meta:
        model = TypeBande
        fields = ['libelle']
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control'})
        }

class BandeForm(forms.ModelForm):
    class Meta:
        model = Bande
        fields = ['batiment', 'code_bande', 'date_debut','date_fin', 'effectif_depart', 'type_bande']
        widgets = {
            'batiment': forms.Select(attrs={'class': 'form-select'}),
            'code_bande': forms.TextInput(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
             'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'effectif_depart': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_bande': forms.Select(attrs={'class': 'form-select'}),
        }

class MortaliteForm(forms.ModelForm):
    class Meta:
        model = Mortalite
        fields = ['date', 'bande', 'effectif', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bande': forms.Select(attrs={'class': 'form-select'}),
            'effectif': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['batiment', 'designation', 'quantite']
        widgets = {
            'batiment': forms.Select(attrs={'class': 'form-select'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import CategorieDepense, DepenseAvicole

class CategorieDepenseForm(forms.ModelForm):
    class Meta:
        model = CategorieDepense
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Alimentation, Médicaments...'
            })
        }
        labels = {
            'nom': 'Nom de la catégorie'
        }

class DepenseAvicoleForm(forms.ModelForm):
    class Meta:
        model = DepenseAvicole
        fields = ['date', 'bande', 'categorie', 'quantite', 'prix_unitaire', 'montant_fcfa', 'description']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'bande': forms.Select(attrs={
                'class': 'form-select'
            }),
            'categorie': forms.Select(attrs={
                'class': 'form-select'
            }),
            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'prix_unitaire': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'montant_fcfa': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'readonly': True  # Montant calculé automatiquement
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Détails de la dépense...'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        quantite = cleaned_data.get('quantite')
        prix_unitaire = cleaned_data.get('prix_unitaire')
        
        # Calcul automatique du montant si les deux champs sont remplis
        if quantite and prix_unitaire:
            cleaned_data['montant_fcfa'] = quantite * prix_unitaire
        
        return cleaned_data