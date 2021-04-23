from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'group', 'email', 'password1', 'password2', ]


#  Лекции
class TrpoLecturesForm(forms.ModelForm):
    """Форма создания новой трпо лекции"""

    class Meta:
        model = TrpoLectures
        fields = '__all__'


class Pp0201LecturesForm(forms.ModelForm):
    """Форма создания новой пп0201 лекции"""

    class Meta:
        model = PP0201Lectures
        fields = '__all__'


class Pp0102LecturesForm(forms.ModelForm):
    """Форма создания новой пп0102 лекции"""

    class Meta:
        model = PP0102Lectures
        fields = '__all__'


#  Практики
class TrpoPracticesForm(forms.ModelForm):
    """Форма создания новой трпо практики"""

    class Meta:
        model = TrpoPractices
        fields = '__all__'


class Pp0201PracticesForm(forms.ModelForm):
    """Форма создания новой пп0201 практики"""

    class Meta:
        model = PP0201Practices
        fields = '__all__'


class Pp0102PracticesForm(forms.ModelForm):
    """Форма создания новой пп0102 практики"""

    class Meta:
        model = PP0102Practices
        fields = '__all__'