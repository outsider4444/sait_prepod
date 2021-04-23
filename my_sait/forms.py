from django import forms
from .models import *


# Изделия
class CalendarForm(forms.ModelForm):
    """Форма календаря выставки оценок"""

    class Meta:
        model = Marks
        fields = '__all__'


#  Лекции
class LecturesForm(forms.ModelForm):
    """Форма создания новой лекции"""

    class Meta:
        model = Lectures
        fields = '__all__'


# Практики
class PracticeForm(forms.ModelForm):
    """Форма создания новой лекции"""

    class Meta:
        model = Practices
        fields = '__all__'
