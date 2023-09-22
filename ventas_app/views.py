# ventas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth import logout
from ventas_app.models import Usuario
from ventas_app.models import marca
from .forms import PerfilForm
from .forms import ProfileImageForm
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse


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


def registro_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:
                hashed_password = make_password(password)
                usuario = form.save(commit=False)
                usuario.password = hashed_password
                image_form = ProfileImageForm(request.POST, request.FILES)
                if image_form.is_valid():
                    usuario.image = image_form.cleaned_data['image']
                usuario.save()
                return redirect('login')
            else:
                form.add_error('password2', 'Las contraseñas no coinciden')
    else:
        form = PerfilForm()
        image_form = ProfileImageForm()
    return render(request, 'auth-register-basic.html', {'form': form, 'image_form': image_form})


def reiniciar_contraseña_view(request):
    return render(request, 'auth-reset-password.html', {})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    # Obtener todos los usuarios
    users = Usuario.objects.all()
    return render(request, 'dashboard.html', {'users': users})


def dashboard_datos(request):
    if not request.user.is_authenticated:
        return redirect('error')
    print(request)
    usuarios = list(Usuario.objects.all().values())
    datos = {'usuarios': usuarios}
    return JsonResponse(datos)


def configperfil_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        print(request.POST)  
        if form.has_changed() and form.is_valid():  
            print(form.errors)
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


def ImagenPerfil_view(request):
     if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('configperfil')  # se redirige a la página de inicio del sistema después de guardar la imagen
        else:
            form = ProfileImageForm(instance=request.user)
            return render(request, 'account-profile_base.html', {'form': form})


def seguridad_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    error_message = None
    success_message = None
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


def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('dashboard')


def error404_view(request):
    return render(request, 'error-404.html', {})


def marcas_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    return render(request, 'marcas/marcas.html', {})


def marcas_datos(request):
    if not request.user.is_authenticated:
        return redirect('error')
    print(request)
    marcas = list(marca.objects.all().values())
    datos = {'marcas': marcas}
    return JsonResponse(datos)


def agregar_marca(request):
    if not request.user.is_authenticated:
        return redirect('error')
    if request.method == 'POST':
        nombre_de_la_marca = request.POST.get('nombre_de_la_marca')
        descripcion = request.POST.get('descripcion')
        marca.objects.create(nombre_de_la_marca=nombre_de_la_marca, descripcion=descripcion)
        return redirect('marcas')
    return render(request, 'marcas/agregar_marca.html', {})


def editar_marca(request):
    if not request.user.is_authenticated:
        return redirect('error')
    return render(request, 'marcas/editar_marcas.html', {})


def eliminar_marca(request):
    if not request.user.is_authenticated:
        return redirect('error')
    return render(request, 'marcas/eliminar_marcas.html', {})

def clientes_view(request):
    if not request.user.is_authenticated:
        return redirect('error')
    return render(request, 'clientes/clientes.html', {})