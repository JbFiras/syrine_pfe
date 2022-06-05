from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Equipe(models.Model):
    nom = models.CharField(max_length=255,null=False,blank=False)
    responsable = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name="responsable")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
       return self.nom