from django.contrib import admin
from .models import Usuario, Marca, Domicilio, DatosContacto, DatosFiscales, DatosPersonales, \
    UsuariosAcceso, Clientes, Negocio, DepartamentoProducto, UnidadesMedidaProducto, Productos, \
    Cajas, MovimientosCaja, Ventas, DetalleVentas

admin.site.register(Usuario)
admin.site.register(Marca)
admin.site.register(Domicilio)
admin.site.register(DatosContacto)
admin.site.register(DatosFiscales)
admin.site.register(DatosPersonales)
admin.site.register(UsuariosAcceso)
admin.site.register(Clientes)
admin.site.register(Negocio)
admin.site.register(DepartamentoProducto)
admin.site.register(UnidadesMedidaProducto)
admin.site.register(Productos)
admin.site.register(Cajas)
admin.site.register(MovimientosCaja)
admin.site.register(Ventas)
admin.site.register(DetalleVentas)
