from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    photo = models.ImageField(null=True, blank=True)
   
    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'


class TypeFournisseur(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

class TypeClient(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle



class Fournisseur(models.Model):
    type = models.ForeignKey(TypeFournisseur, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom


class Client(models.Model):
    type = models.ForeignKey(TypeClient, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
