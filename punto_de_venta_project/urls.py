# punto_de_venta_project/urls.py

from django.contrib import admin
from django.urls import path, include
from ventas_app import views  # Asegúrate de importar las vistas de la aplicación "ventas"
from django.conf import settings
from django.conf.urls.static import static

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
    path('error404/',views.error404_view, name='error'),
    path('editarImagen/',views.ImagenPerfil_view, name='imagenPerfil'),
    path('lista_usuarios/', views.dashboard_datos, name='lista_usuarios'),
    path('marcas/', views.marcas_view, name='marcas'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
