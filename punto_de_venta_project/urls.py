# punto_de_venta_project/urls.py

from django.contrib import admin
from django.urls import path, include
from ventas_app import views  # Asegúrate de importar las vistas de la aplicación "ventas"

urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),  # Redireccionar URL raíz a la página de inicio
    path('', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('admin/', admin.site.urls),
]
