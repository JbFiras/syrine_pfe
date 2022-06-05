from tabnanny import verbose
from django.db import models
from accounts.models import *
# Create your models here.


class Reclamation_Probleme_Maintenance(models.Model):
    responsable = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user")
    nom = models.CharField(max_length=255,null=False,blank=False)
    commentaire = models.TextField(max_length=255,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.nom


class Reclamation_Manque_Piece(models.Model):
    responsable = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_manque_piece")
    nom = models.CharField(max_length=255,null=False,blank=False)
    reference = models.CharField(max_length=255,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.reference



class Reclamation_Probleme_Quanlite(models.Model):
    responsable = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_probleme_qualite")
    nom = models.CharField(max_length=255,null=False,blank=False)
    reference = models.CharField(max_length=255,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.reference



class Objectif_Production(models.Model):
    equipe = models.OneToOneField(Equipe, null=True, on_delete=models.CASCADE, related_name="equipe")
    limite = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return self.equipe

    class META:
        verbose_name = "Objectif de Production"