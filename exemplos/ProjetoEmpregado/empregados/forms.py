from django import forms
from .models import Empregado

class EmpregadoForm(forms.ModelForm):
    class Meta:
        model = Empregado
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cargo', 'data_contratacao']
