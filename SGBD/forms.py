from django import forms
from SGBD.models import Empleado
from SGBD.models import Animal
from SGBD.models import Alimentacion

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model =  Empleado
        fields = "__all__"

class AnimalForm(forms.ModelForm):
    class Meta:
        model =  Animal
        fields = "__all__"

class AlimentacionForm(forms.ModelForm):
    class Meta:
        model = Alimentacion
        fields= "__all__"
