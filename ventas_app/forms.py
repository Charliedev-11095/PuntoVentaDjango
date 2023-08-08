# ventas/forms.py

# ventas/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['username','nombre', 'email' , 'password1', 'password2', 'first_name', 'last_name','gender','birth_date','is_staff', 'es_vendedor']

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class':'form-control'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_staff'].widget.attrs.update({'class': ''})
        self.fields['es_vendedor'].widget.attrs.update({'class': ''})