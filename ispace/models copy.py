from django.db import models
import re
# Create your models here.
class Batiment(models.Model):
    TYPE_CHOICES = [
        ('elevage', 'Élevage'),
        ('nourriture', 'Stockage de nourriture'),
        ('autre', 'Autre'),
    ]

    code = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=100)  # Ex: "10x5"
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='autre')

    def __str__(self):
        return f"{self.code} - {self.designation}"

    @property
    def unite_capacite(self):
        if self.type == 'elevage':
            return f"{self.capacite} têtes"
        elif self.type == 'nourriture':
            return f"{self.capacite} kg"
        else:
            return f"{self.capacite} unités"

    def superficie(self):
        try:
            # Nettoyer l’entrée et séparer longueur et largeur
            dimensions = self.dimensions.lower().replace('m', '').replace(' ', '')
            longueur, largeur = map(float, dimensions.split('x'))
            surface = longueur * largeur
            return f"{surface:.2f} m²"
        except:
            return "N/A"


            



class TypeBande(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle
class Bande(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    code_bande = models.CharField(max_length=50, unique=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    effectif_depart = models.PositiveIntegerField()
    type_bande = models.ForeignKey(TypeBande, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.code_bande} ({self.batiment.designation})"

    @property
    def periode(self):
        return f"{self.date_debut.strftime('%d/%m/%Y')} - {self.date_fin.strftime('%d/%m/%Y')}"

class Mortalite(models.Model):
    date = models.DateField()
    bande = models.ForeignKey(Bande, on_delete=models.CASCADE)
    effectif = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
     return f"{self.bande.code_bande} - {self.date} - {self.effectif} morts"

class Materiel(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100,null=True, blank=True)
    quantite = models.PositiveIntegerField(null=True, blank=True)
    date_ajout = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.designation


class CategorieDepense(models.Model):
    nom = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nom

class DepenseAvicole(models.Model):
    date = models.DateField(null=True, blank=True)
    bande = models.ForeignKey(Bande, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategorieDepense, on_delete=models.PROTECT)
    quantite = models.FloatField(null=True, blank=True)
    prix_unitaire = models.FloatField(null=True, blank=True)
    montant_fcfa = models.FloatField(null=True, blank=True, verbose_name="Montant (FCFA)")
    description = models.TextField(null=True, blank=True)

def save(self, *args, **kwargs):
        """Calcule automatiquement le montant si quantite et prix_unitaire sont renseignés"""
        if self.quantite and self.prix_unitaire:
            self.montant_fcfa = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)

def __str__(self):
        return f"Dépense {self.categorie.nom} - {self.bande.code_bande} - {self.date}"

@property
def montant(self):
        """Propriété pour rétro-compatibilité"""
        return self.montant_fcfa