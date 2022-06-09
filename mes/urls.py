from django.urls import path,include,re_path
from . import views


app_name="mes"

urlpatterns = [

    path('reclamation/',views.ReclamationPage, name="reclamation-page"),
    path('dashboard/',views.AcceuilPage, name="acceuil-page"),
    path('demarrage-de-la-ligne/',views.DemarrageDeLaLignePage, name="demarrage-de-la-ligne-page"),
    path('reclamation-manque-piece/',views.reclamationManquePiecePage, name="reclamation-manque-piece-page"),
    path('reclamation-probleme-qualite/',views.reclamationProblemeQualitePage, name="reclamation-probleme-qualite-page"),
    path('commencer-reunion/',views.CommencerunereunionPage, name="commencer-reunion-page"),
    path('mode-hors-ligne/',views.ModeHorsLignePage, name="mode-hors-ligne-page"),
    path('pause/',views.PausePage, name="pause-page"),
    path('statistique/',views.StatistiquesPage, name="statistique-page"),
    path('fin-equipe/',views.FinEquipePage, name="fin-equipe-page"),
    
    
    

]