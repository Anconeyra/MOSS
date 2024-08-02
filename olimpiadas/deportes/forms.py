from django import forms
from .models import Archivo
from .models import Categoria

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'logo']
