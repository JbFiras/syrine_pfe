from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def HomePage(request):
    return render(request, "home.html")


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('mes:acceuil-page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user :
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Bienvenue')
                    return redirect('mes:acceuil-page')

            else:
                messages.error(request, 'Le nom d utilisateur ou le mot de passe sont incorrects!!')
                return redirect('accounts:login-page')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('accounts:login-page')


def error_404_view(request,exception):  
    return render(request,'home.html')
