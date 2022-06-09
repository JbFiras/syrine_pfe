from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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
    if request.method == 'GET':
        messages.success(request, 'démarrage de la ligne')
        return redirect('mes:acceuil-page')

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



@login_required
def StatistiquesPage(request):
    user = request.user
    total_probleme_de_maintenance = Reclamation_Probleme_Maintenance.objects.filter(responsable=user).count()
    total_reclamation_manque_piece = Reclamation_Manque_Piece.objects.filter(responsable=user).count()
    total_reclamation_probleme_qualite = Reclamation_Probleme_Quanlite.objects.filter(responsable=user).count()

    context={
        "total_probleme_de_maintenance":total_probleme_de_maintenance,
        "total_reclamation_manque_piece":total_reclamation_manque_piece,
        "total_reclamation_probleme_qualite":total_reclamation_probleme_qualite,
    }
    return render(request, "statistiques.html",context)



@login_required
def FinEquipePage(request):
    if request.method == 'POST':
        form = Produced_Product_NumberForm(request.POST)
        if form.is_valid():
            equipe = Equipe.objects.filter(responsable=request.user).first()
            user = form.save()
            user.equipe = equipe
            user.save()
            produced_product = int(user.objectif)
            objectif = Objectif_Production.objects.filter(equipe=equipe).first()
            objectif_value = int(objectif.objectif)
            if objectif_value > produced_product:
                result = objectif_value - produced_product
                messages.error(request, f'Objectif de production n est pas atteint, il manque :' +str(result) +" pieces")
                return HttpResponseRedirect(request.META["HTTP_REFERER"])

            if objectif_value < produced_product:
                result =  produced_product - objectif_value
                messages.success(request, f'Félicitation, Objectif de production est dépassé avec:  ' +str(result) +" pieces")
                return HttpResponseRedirect(request.META["HTTP_REFERER"])

            if objectif_value == produced_product:
                messages.success(request, f'Félicitation, Object de production atteint ')
                return HttpResponseRedirect(request.META["HTTP_REFERER"])
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return render(request, "fin_d_equipe.html")