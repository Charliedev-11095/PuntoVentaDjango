# ventas/forms.py
from django import forms
from .models import Usuario
from .models import Marca

class RegistroForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PerfilForm(forms.ModelForm):
    # profile_picture = forms.ImageField(label='Foto de perfil', required=False)
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = Usuario
        fields = ['user_name','email','nombre', 'apellido_paterno', 'apellido_materno', 'gender', 'phone', 'birth_date','image','is_active','is_staff', 'es_vendedor']
      
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control','id':'inputBirthday'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update()
        self.fields['is_staff'].widget.attrs.update()
        self.fields['es_vendedor'].widget.attrs.update()
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['image']


def __init__(self, *args, **kwargs):
    super(ProfileImageForm, self).__init__(*args, **kwargs)
    self.fields['image'].widget.attrs.update({'class': 'form-control'})


class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre_de_la_marca', 'descripcion_marca',]


        class meta:
            model = Marca
            fields = ['nombre_de_la_marca', 'descripcion_marca']

    def __init__(self, *args, **kwargs):
        super(MarcasForm, self).__init__(*args, **kwargs)
        self.fields['nombre_de_la_marca'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion_marca'].widget.attrs.update({'class': 'form-control'})

