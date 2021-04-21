from django import forms
from .models import *


# Изделия
class CalendarForm(forms.ModelForm):
    """Форма изделий"""

    class Meta:
        model = Calendar
        fields = '__all__'
