from django import forms
from .models import Rezervacija

class RezervacijaForm(forms.ModelForm):
    class Meta:
        model = Rezervacija
        fields = '__all__'