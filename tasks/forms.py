from django.forms import ModelForm
from .models import Equipo

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'pais', 'fecha_creacion', 'entrenador']