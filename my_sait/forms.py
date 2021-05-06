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


# Оценки
class CreateMarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'
        widgets = {
            'date' : forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['users_code'].queryset = Marks.objects.none()

        if 'group' in self.data:
            try:
                group = int(self.data.get('group'))
                self.fields['users_code'].queryset = Marks.objects.filter(users_code__group=group).order_by('users_code__name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['users_code'].queryset = self.instance.users_code.marks_set.order_by('users_code__name')
