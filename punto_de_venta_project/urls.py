# punto_de_venta_project/urls.py

from django.contrib import admin
from django.urls import path, include
from ventas_app import views  # Asegúrate de importar las vistas de la aplicación "ventas"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('configperfil/',views.configperfil_view,name='configperfil'),
    path('pago/', views.pago_view, name='pago'),
    path('seguridad/', views.seguridad_view, name='seguridad'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('registro/', views.registro_view, name='registro'),
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('error404/',views.error404_view, name='error')

]
