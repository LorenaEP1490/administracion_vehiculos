from django import forms
from .models import InspeccionAccesorios, InspeccionMecanica, InspeccionExterior, InspeccionInterior

# 🔧 Formulario de Inspección de Accesorios
class InspeccionAccesoriosForm(forms.ModelForm):
    class Meta:
        model = InspeccionAccesorios
        fields = "__all__"

    cricket = forms.BooleanField(required=False, label="Cricket (Sí/No)")
    matafuegos = forms.BooleanField(required=False, label="Matafuegos (Sí/No)")
    navegador = forms.BooleanField(required=False, label="Navegador (Sí/No)")
    bateria = forms.BooleanField(required=False, label="Batería (Sí/No)")
    bateria_marca = forms.CharField(required=False, label="Marca de Batería")
    bateria_amperaje = forms.CharField(required=False, label="Amperaje de Batería")
    stereo_tiene = forms.BooleanField(required=False, label="Stereo (Tiene/No Tiene)")
    stereo_funciona = forms.BooleanField(required=False, label="Stereo Funciona (Sí/No)")
    stereo_marca = forms.CharField(required=False, label="Marca del Stereo")
    tuercas_seguridad = forms.BooleanField(required=False, label="Tuercas de Seguridad (Sí/No)")
    manuales = forms.BooleanField(required=False, label="Manuales (Sí/No)")
    duplicado_llaves = forms.BooleanField(required=False, label="Duplicado de Llaves (Sí/No)")
    observaciones = forms.CharField(widget=forms.Textarea, required=False, label="Observaciones")

# 🔧 Formulario de Inspección Mecánica
class InspeccionMecanicaForm(forms.ModelForm):
    class Meta:
        model = InspeccionMecanica
        fields = "__all__"

    motor = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Estado del Motor")
    niveles_liquidos = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Niveles de Líquidos")
    bateria_estado = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente")], label="Estado de la Batería")
    transmision = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Transmisión")
    frenos = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Frenos")
    suspension = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Suspensión")
    escape = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Escape")
    emisiones = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Emisiones")
    embrague = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Embrague")
    observaciones = forms.CharField(widget=forms.Textarea, required=False, label="Observaciones")

# 🚗 Formulario de Inspección Exterior
class InspeccionExteriorForm(forms.ModelForm):
    class Meta:
        model = InspeccionExterior
        fields = "__all__"

    carroceria = forms.BooleanField(required=False, label="Carrocería (Daños Sí/No)")
    carroceria_detalle = forms.CharField(required=False, label="Detalles de Daños en Carrocería")
    pintura = forms.BooleanField(required=False, label="Pintura (Sí/No)")
    pintura_detalle = forms.CharField(required=False, label="Detalles de Pintura")
    parabrisas = forms.BooleanField(required=False, label="Parabrisas y Ventanas (Sí/No)")
    parabrisas_detalle = forms.CharField(required=False, label="Detalles de Parabrisas")
    faros = forms.BooleanField(required=False, label="Faros y Luces (Sí/No)")
    faros_detalle = forms.CharField(required=False, label="Detalles de Faros")
    neumaticos = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Estado de Neumáticos")
    espejos = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Espejos Retrovisores")
    limpiaparabrisas = forms.ChoiceField(choices=[("Aprobado", "Aprobado"), ("Deficiente", "Deficiente"), ("Requiere Atención", "Requiere Atención")], label="Limpiaparabrisas")
    observaciones = forms.CharField(widget=forms.Textarea, required=False, label="Observaciones")

# 🛋 Formulario de Inspección Interior
class InspeccionInteriorForm(forms.ModelForm):
    class Meta:
        model = InspeccionInterior
        fields = "__all__"

    asientos = forms.ChoiceField(choices=[("Buen Estado", "Buen Estado"), ("Dañado", "Dañado"), ("Requiere Atención", "Requiere Atención")], label="Estado de Asientos")
    tablero = forms.ChoiceField(choices=[("Buen Estado", "Buen Estado"), ("Dañado", "Dañado"), ("Requiere Atención", "Requiere Atención")], label="Estado del Tablero")
    climatizacion = forms.ChoiceField(choices=[("Buen Estado", "Buen Estado"), ("Dañado", "Dañado"), ("Requiere Atención", "Requiere Atención")], label="Sistema de Climatización")
    audio = forms.ChoiceField(choices=[("Funciona", "Funciona"), ("No Funciona", "No Funciona")], label="Sistema de Audio")
    alfombras = forms.ChoiceField(choices=[("Buen Estado", "Buen Estado"), ("Dañado", "Dañado"), ("Requiere Atención", "Requiere Atención")], label="Estado de Alfombras")
    airbag = forms.ChoiceField(choices=[("Funciona", "Funciona"), ("No Funciona", "No Funciona")], label="Estado del Airbag")
    observaciones = forms.CharField(widget=forms.Textarea, required=False, label="Observaciones")
