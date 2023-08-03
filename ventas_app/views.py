# ventas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import RegistroForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

def login_view(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))  # Redirecciona a la página de inicio del sistema
        else:
            error_message = "Usuario inválido. Por favor, inténtalo de nuevo."
    
    return render(request, 'auth-login-basic.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de inicio de sesión después del logout

from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambiar por la URL a la que se redireccionará después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'auth-register-basic.html', {'form': form})


def dashboard_view(request):
    return render(request, 'dashboard.html', {})

def editperfildashboard_view(request):
    return render(request, 'account-profile_base.html', {})

