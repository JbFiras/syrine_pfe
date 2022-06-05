from django import forms
from django.forms import ModelForm
from .models import  *


class ReclamationForm(ModelForm):
    class Meta:
        model = Reclamation_Probleme_Maintenance
        fields =  '__all__'
        exclude = ['created_at','responsable']


class Reclamation_Manque_PieceForm(ModelForm):
    class Meta:
        model = Reclamation_Manque_Piece
        fields =  '__all__'
        exclude = ['created_at','responsable']



class Reclamation_Probleme_QuanliteForm(ModelForm):
    class Meta:
        model = Reclamation_Probleme_Quanlite
        fields =  '__all__'
        exclude = ['created_at','responsable']

