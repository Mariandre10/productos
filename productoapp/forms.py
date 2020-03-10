from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils import timezone
from .models import Producto

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Username'}),
    label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}),
    label="Password")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'code', 'fabricante', 'origen', 'precio']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'code': forms.TextInput(attrs={'class':'form-control','placeholder':'Code'}),
            'fabricante': forms.TextInput(attrs={'class':'form-control','placeholder':'Fabricante'}),
            'origen': forms.TextInput(attrs={'class':'form-control','placeholder':'Origen'}),
            'precio': forms.TextInput(attrs={'class':'form-control','placeholder':'Precio'})
        }