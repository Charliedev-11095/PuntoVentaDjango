# ventas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import RegistroForm
from django.contrib.auth import logout
from ventas_app.models import Usuario
from .forms import PerfilForm
from django.contrib import messages

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
    if not request.user.is_authenticated:
        return redirect('error')
    # Obtener todos los usuarios
    users = Usuario.objects.all()
    return render(request, 'dashboard.html', {'users': users})

def configperfil_view(request):
    if not request.user.is_authenticated:
        return redirect('error')

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.has_changed():
            if form.is_valid():
                form.save()
                return redirect('dashboard')
    else:
        form = PerfilForm(instance=request.user)
    error_messages = []
    if 'user_name' in form.errors:
        error_messages.append("Error: El campo 'Nombre de usuario' es obligatorio. Por favor, asegúrese de llenar este campo.")
    if 'email' in form.errors:
        error_messages.append("Error: El formato del correo electrónico no es válido. Asegúrese de ingresar una dirección de correo válida.")
    if 'phone' in form.errors:
        error_messages.append("Error: El número de teléfono no tiene el formato correcto. Por favor, ingrese un número válido.")
    if 'gender' in form.errors:
        error_messages.append("Error: Debe seleccionar una opción de género. Asegúrese de elegir entre 'Masculino', 'Femenino' u 'Otro'.")
    if 'birth_date' in form.errors:
        error_messages.append("Error: El formato de la fecha de nacimiento no es válido. Ingrese la fecha en el formato correcto.")
    return render(request, 'account-profile_base.html', {'form': form, 'error_messages': error_messages})

def seguridad_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    error_message = None  # Mensaje de error por defecto
    success_message = None  # Mensaje de éxito por defecto
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')
        if request.user.check_password(current_password):
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                success_message = '¡Contraseña actualizada correctamente!'
            else:
                error_message = 'La nueva contraseña y la confirmación no coinciden.'
        else:
            error_message = 'La contraseña actual es incorrecta.'
    
    return render(request, 'account-security.html', {'error_message': error_message, 'success_message': success_message})

def pago_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    return render(request, 'account-billing.html', {})

def error404_view(request):
    return render(request, 'error-404.html', {})


