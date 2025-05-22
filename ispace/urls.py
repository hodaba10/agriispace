from django.contrib import admin
from django.urls import path 
from ispace import views
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard , name='dashboard'),
    path('batiment/', views.BatimentListView.as_view(), name='batiment_list'),
    path('batiment/ajouter/', views.BatimentCreateView.as_view(), name='batiment_add'),
    path('batiment/<int:pk>/modifier/', views.BatimentUpdateView.as_view(), name='batiment_edit'),
    path('batiment/<int:pk>/supprimer/', views.BatimentDeleteView.as_view(), name='batiment_delete'),
        
    
    # TypeBande
    path('type-bande/', views.TypeBandeListView.as_view(), name='type_bande_list'),
    path('type-bande/ajouter/', views.TypeBandeCreateView.as_view(), name='type_bande_add'),
    path('type-bande/<int:pk>/modifier/', views.TypeBandeUpdateView.as_view(), name='type_bande_edit'),
    path('type-bande/<int:pk>/supprimer/', views.TypeBandeDeleteView.as_view(), name='type_bande_delete'),
    
    # Bande
    path('bandes/', views.BandeListView.as_view(), name='bande_list'),
    path('bandes/ajouter/', views.BandeCreateView.as_view(), name='bande_add'),
    path('bandes/<int:pk>/', views.BandeDetailView.as_view(), name='bande_detail'),
    path('bandes/<int:pk>/modifier/', views.BandeUpdateView.as_view(), name='bande_edit'),
    path('bandes/<int:pk>/supprimer/', views.BandeDeleteView.as_view(), name='bande_delete'),
    # Mortalité
    path('mortalites/', views.MortaliteListView.as_view(), name='mortalite_list'),
    path('mortalites/ajouter/', views.MortaliteCreateView.as_view(), name='mortalite_add'),
    path('mortalites/<int:pk>/modifier/', views.MortaliteUpdateView.as_view(), name='mortalite_edit'),
    path('mortalites/<int:pk>/supprimer/', views.MortaliteDeleteView.as_view(), name='mortalite_delete'),
    
    # Matériel
    path('materiels/', views.MaterielListView.as_view(), name='materiel_list'),
    path('materiels/ajouter/', views.MaterielCreateView.as_view(), name='materiel_add'),
    path('materiels/<int:pk>/modifier/', views.MaterielUpdateView.as_view(), name='materiel_edit'),
    path('materiels/<int:pk>/supprimer/', views.MaterielDeleteView.as_view(), name='materiel_delete'),
    
    # Dépenses
    path('depenses/', views.DepenseAvicoleListView.as_view(), name='depense_list'),
    path('depenses/ajouter/', views.DepenseAvicoleCreateView.as_view(), name='depense_add'),
    path('depenses/<int:pk>/modifier/', views.DepenseAvicoleUpdateView.as_view(), name='depense_edit'),
    path('depenses/<int:pk>/supprimer/', views.DepenseAvicoleDeleteView.as_view(), name='depense_delete'),
    
    
    path('categories-depense/', views.CategorieDepenseListView.as_view(), name='categorie_depense_list'),
    path('categories-depense/ajouter/', views.CategorieDepenseCreateView.as_view(), name='categorie_depense_add'),
    path('categories-depense/<int:pk>/modifier/', views.CategorieDepenseUpdateView.as_view(), name='categorie_depense_edit'),
    path('categories-depense/<int:pk>/supprimer/', views.CategorieDepenseDeleteView.as_view(), name='categorie_depense_delete'),
]
