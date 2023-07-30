# ventas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirecciona a la página de inicio del sistema
        else:
            error_message = "Credenciales inválidas. Por favor, inténtalo de nuevo."
    else:
        error_message = ""
    return render(request, 'login.html', {'error_message': error_message})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def dashboard_view(request):
    return render(request, 'ventas/dashboard.html', {})
