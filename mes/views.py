from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ReclamationPage(request):
    form = ReclamationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.responsable = request.user
            user.save()
            messages.success(request, 'Reclamation enregistré avec success')
            return redirect('mes:acceuil-page')
    return render(request, "reclamation.html")


@login_required
def AcceuilPage(request):
    user = request.user
    total_probleme_de_maintenance = Reclamation_Probleme_Maintenance.objects.filter(responsable=user).count()
    total_reclamation_manque_piece = Reclamation_Manque_Piece.objects.filter(responsable=user).count()
    total_reclamation_probleme_qualite = Reclamation_Probleme_Quanlite.objects.filter(responsable=user).count()

    context={
        "total_probleme_de_maintenance":total_probleme_de_maintenance,
        "total_reclamation_manque_piece":total_reclamation_manque_piece,
        "total_reclamation_probleme_qualite":total_reclamation_probleme_qualite,
    }
    return render(request, "acceuil.html",context)


@login_required
def DemarrageDeLaLignePage(request):
    return render(request, "demarragedelaligne.html")

@login_required
def CommencerunereunionPage(request):
    return render(request, "reunion.html")

@login_required
def ModeHorsLignePage(request):
    return render(request, "mode_hors_ligne.html")

@login_required
def PausePage(request):
    return render(request, "pause.html")


@login_required
def reclamationManquePiecePage(request):
    form = Reclamation_Manque_PieceForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.responsable = request.user
            user.save()
            messages.success(request, 'Reclamation enregistré avec success')
            return redirect('mes:acceuil-page')
    return render(request, "reclamationmanquepiece.html")



@login_required
def reclamationProblemeQualitePage(request):
    form = Reclamation_Probleme_QuanliteForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.responsable = request.user
            user.save()
            messages.success(request, 'Reclamation enregistré avec success')
            return redirect('mes:acceuil-page')
    return render(request, "reclamationproblemequalite.html")