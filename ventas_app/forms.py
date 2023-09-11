# ventas/forms.py
from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PerfilForm(forms.ModelForm):
    profile_picture = forms.ImageField(label='Foto de perfil', required=False)

    class Meta:
        model = Usuario
        fields = ['user_name','email','nombre', 'apellido_paterno','password','password2', 'apellido_materno', 'gender', 'phone', 'birth_date','image','is_staff', 'es_vendedor']

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_staff'].widget.attrs.update()
        self.fields['es_vendedor'].widget.attrs.update()

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['image']


def __init__(self, *args, **kwargs):
    super(ProfileImageForm, self).__init__(*args, **kwargs)
    self.fields['image'].widget.attrs.update({'class': 'form-control'})



