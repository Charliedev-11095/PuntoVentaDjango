# Create your models here.
from django.db import models
from django.conf import settings 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms

class UsuarioManager(BaseUserManager):
    def create_user(self, user_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El campo de correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Los superusuarios deben tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Los superusuarios deben tener is_superuser=True.")
        return self.create_user(user_name, email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]
    user_name=models.CharField(("Usuario"),max_length=50,unique=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellido_paterno=models.CharField(max_length=30, blank=True)
    apellido_materno=models.CharField(max_length=30, blank=True)
    email = models.EmailField(("Correo"),unique=True)
    password = models.CharField(("Contraseña"), max_length=128)
    password1 = models.CharField(("Nueva contraseña"), max_length=128)
    password2 = models.CharField(("Confirmar contraseña"), max_length=128)
    gender = models.CharField(("género"),max_length=9, choices=GENDER_CHOICES, blank=True)
    phone = models.CharField(("Téléfono"),max_length=10, blank=True)
    birth_date = models.DateField(("Fecha de Nacimiento"),null=True, blank=True)
    image = models.ImageField(("Imagen"), upload_to='profile_pics', blank=True)
    is_active = models.BooleanField(("está activo"),default=True)
    is_staff = models.BooleanField(("es trabajador"),default=False)
    es_vendedor = models.BooleanField(("es vendedor"),default=False)
    is_superuser = models.BooleanField(("es superusuario"),default=False)
    objects = UsuarioManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class CambioContraseñaForm(forms.Form):
    currentPassword = forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newPassword = forms.CharField(label="Contraseña Nueva", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmPassword = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#Tabla Marcas
class marca(models.Model):
    descripcion = models.CharField(max_length=50,null=False)

class Domicilio(models.Model):
    calle = models.CharField(max_length=50,null=False)
    no_exterior = models.CharField(max_length=50,null=False)
    pais = models.CharField(max_length=50,null=False)
    codigo_postal = models.CharField(max_length=50,null=False)
    municipio = models.CharField(max_length=50,null=False)
    estado = models.CharField(max_length=50,null=False)
    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilio'


class DatosContacto(models.Model):
    telefono = models.CharField(max_length=10, null=True)
    celular = models.CharField(max_length=10,null=False)
    correo_electronico = models.EmailField(max_length=250, null=True)
    url_social = models.URLField(max_length=250,null=True)

class DatosFiscales(models.Model):
    rfc = models.CharField(max_length=13, null=True)
    razon_social = models.CharField(max_length=50, null=True)
    direccion = models.ForeignKey(Domicilio, null=False, blank=False,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Dato Fiscal'
        verbose_name_plural = 'Datos Fiscales'


class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    genero = models.CharField(max_length=1,null=True)

    class Meta:
        verbose_name = 'Dato Personal'
        verbose_name_plural = 'Datos Personales'

#Tabla Usuarios Acceso
class UsuariosAcceso(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales,null=False,on_delete=models.CASCADE)
    datos_contacto = models.ForeignKey(DatosContacto,null=False,on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=50,null=False)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1)

#Tabla de clientes
class Clientes(models.Model):
    datos_personales = models.ForeignKey(DatosPersonales,null=False,on_delete=models.CASCADE)
    datos_contacto = models.ForeignKey(DatosContacto,null=False,blank=False,on_delete=models.CASCADE)
    datos_fiscales = models.ForeignKey(DatosFiscales,null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Negocio(models.Model):
    contacto = models.ForeignKey(DatosContacto, null=False, blank=False,on_delete=models.CASCADE)
    datos_fiscales = models.ForeignKey(DatosFiscales, null=False,on_delete=models.CASCADE)

class DepartamentoProducto(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)

class UnidadesMedidaProducto(models.Model):
    descripcion = models.CharField(max_length=50,null=False,blank=False)

class Productos(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    descripcion = models.CharField(max_length=300,null=True)
    marca = models.ForeignKey(marca,null=True,blank=False,on_delete=models.SET_NULL)
    existencia = models.DecimalField(max_digits=5,decimal_places=2,null=False,blank=False)
    deparamento_producto = models.ForeignKey(DepartamentoProducto,null=True,blank=False,on_delete=models.SET_NULL)
    precio_venta = models.DecimalField(max_digits=5,decimal_places=2,null=False)
    existencio_minima = models.DecimalField(max_digits=5,decimal_places=2,null=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

#Tabla de cajas
class Cajas(models.Model):
    clave = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

OPCIONMOVIMIENTO = (
    ('a','abrir'),
    ('c','cerrar')
)

class MovimientosCaja(models.Model):
    caja = models.ForeignKey(Cajas,null=True,blank=False, on_delete=models.SET_NULL)
    fecha_apertura = models.DateTimeField()
    fecha_cierre = models.DateTimeField()
    tipo_movimiento = models.CharField(max_length=1,choices=OPCIONMOVIMIENTO)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(UsuariosAcceso,null=True,blank=False,on_delete=models.SET_NULL)
    

#tabla ventas 
METODOPAGOS = (
    ('a','transferencia'),
    ('b','efectivo'),
    ('c','tarjeta de credito'),
    ('d','tarjeta de debito'),
)

class Ventas(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Clientes,null=True,blank=False, on_delete=models.SET_NULL)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Cajas,null=True,blank=False, on_delete=models.SET_NULL)
    metodo_pago = models.CharField(max_length=1, choices=METODOPAGOS)
    importe_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    vuelto = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(UsuariosAcceso,null=True,blank=False, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetalleVentas(models.Model):
    producto = models.ForeignKey(Productos,null=True,blank=False,on_delete=models.SET_NULL)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2)
    venta = models.ForeignKey(Ventas,null=True,blank=False,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
    
    