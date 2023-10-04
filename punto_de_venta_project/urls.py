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
    path('configperfil/editar/<int:usuario_id>/',views.configperfil_view,name='configperfil'),
    path('pago/', views.pago_view, name='pago'),
    path('seguridad/', views.seguridad_view, name='seguridad'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('registro/', views.registro_view, name='registro'),
    path('reiniciar_contraseña/', views.reiniciar_contraseña_view, name='reiniciar_contraseña'),  
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('error404/',views.error404_view, name='error'),
    path('editarImagen/',views.ImagenPerfil_view, name='imagenPerfil'),
    path('lista_usuarios/', views.dashboard_datos, name='lista_usuarios'),
    path('marcas/', views.marcas_view, name='marcas'),
    path('lista_marcas/', views.marcas_datos, name='marcas_datos'),
    path('agregar_marca/', views.agregar_marca, name='agregar_marca'),
    path('editar_marca/<int:marca_id>/', views.editar_marca, name='editar_marca'),
    path('eliminar_marca/', views.eliminar_marca, name='eliminar_marca'),
    path('clientes/', views.clientes_view, name='clientes'),
    # path('lista_clientes/', views.clientes_datos, name='clientes_datos'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    # path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    # path('eliminar_cliente/', views.eliminar_cliente, name='eliminar_cliente'),
    # path('productos/', views.productos_view, name='productos'),
    # path('lista_productos/', views.productos_datos, name='productos_datos'),
    # path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    # path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    # path('eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),
    # path('ventas/', views.ventas_view, name='ventas'),
    # path('lista_ventas/', views.ventas_datos, name='ventas_datos'),
    # path('agregar_venta/', views.agregar_venta, name='agregar_venta'),
    # path('editar_venta/<int:venta_id>/', views.editar_venta, name='editar_venta'), 
    # path('eliminar_venta/', views.eliminar_venta, name='eliminar_venta'),
    # path('ventas/', views.ventas_view, name='ventas'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
