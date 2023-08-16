# ventas/forms.py
from django import forms
from .models import Usuario

from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['nombre','email', 'apellido_paterno','apellido_materno', 'gender', 'phone', 'birth_date','is_staff', 'es_vendedor']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_paterno'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido_materno'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class':'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['es_vendedor'].widget.attrs.update({'class': ''})
        self.fields['is_staff'].widget.attrs.update({'class': ''})
