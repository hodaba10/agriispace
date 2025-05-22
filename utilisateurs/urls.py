from django.contrib import admin
from django.urls import path 
from utilisateurs import views

urlpatterns = [
    
    path('utilisateurs', views.utilisateur , name='utilisateurs'),
    path('utilisateurs/creer/', views.creer_utilisateur, name='creer_utilisateur'),
    path('login', views.login_page , name='login'),
    path('authentification', views.authentification , name='authentification'),
    path('deconnexion', views.deconnexion , name='deconnexion'),
    
     path('', views.ClientListView.as_view(), name='client_list'),
    path('ajouter/', views.ClientCreateView.as_view(), name='client_add'),
    path('<int:pk>/modifier/', views.ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/supprimer/', views.ClientDeleteView.as_view(), name='client_delete'),
]
