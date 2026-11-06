from django import forms
from .models import Pregunta, Respuesta

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['texto', 'email', 'fuentes']