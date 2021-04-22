from django import forms
from .models import *


# Изделия
class CalendarForm(forms.ModelForm):
    """Форма календаря выставки оценок"""

    class Meta:
        model = Calendar
        fields = '__all__'


# ТРПО лекции
class TrpoLecturesForm(forms.ModelForm):
    """Форма создания новой лекции"""

    class Meta:
        model = Lectures
        fields = '__all__'


# ТРПО практики
class TrpoPracticeForm(forms.ModelForm):
    """Форма создания новой лекции"""

    class Meta:
        model = Practices
        fields = '__all__'
