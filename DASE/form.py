from django import forms
#from miApp.models import Tema, Libro

class LibroForm(forms.ModelForm):
    ....
    ....
    temas = forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)