import os
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView

from .forms import CalendarForm, PracticeForm, LecturesForm
from .models import *


def main(request):
    return render(request, 'main/main.html',)

# ТРПО

# Лекции
def trpo_lecture(request):
    lectures = Lectures.objects.filter(items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"lectures": lectures,}
    return render(request, 'items/trpo/lectures_list.html', context)


def trpo_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = LecturesForm()
    error = ""
    if request.method == "POST":
        form = LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('trpo_lectures'))
        else:
            error = form.errors
    return render(request, "items/trpo/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
def trpo_practice(request):
    practice = Practices.objects.filter(items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"practice": practice,}
    return render(request, 'items/trpo/practices_list.html', context)


def trpo_New_practice(request):
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = PracticeForm()
    error = ""
    if request.method == "POST":
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('trpo_lectures'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "items/trpo/forms/practice_new.html", {"form": form, "error": error, "item": item})


# ПП.02.01

# Лекции
def pp0201_lecture(request):
    lectures = Lectures.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'items/pp0201/lectures_list.html', context)


def pp0201_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name='ПП.02.01. Прикладное программирование')
    form = LecturesForm()
    error = ""
    if request.method == "POST":
        form = LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0201_lectures'))
        else:
            error = form.errors
    return render(request, "items/pp0201/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
def pp0201_practice(request):
    practice = Practices.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"practice": practice,}
    return render(request, 'items/pp0201/practices_list.html', context)


def pp0201_New_practice(request):
    item = Items.objects.get(name='ПП.02.01. Прикладное программирование')
    form = PracticeForm()
    error = ""
    if request.method == "POST":
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0201_lectures'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "items/pp0201/forms/practice_new.html", {"form": form, "error": error, "item": item})


# ПП.01.02

# Лекции
def pp0102_lecture(request):
    lectures = Lectures.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'items/pp0102/lectures_list.html', context)


def pp0102_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name="ПП.01.02. Прикладное программирование")
    form = LecturesForm()
    error = ""
    if request.method == "POST":
        form = LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0102_lectures'))
        else:
            error = form.errors
    return render(request, "items/pp0102/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
def pp0102_practice(request):
    practice = Practices.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"practice": practice,}
    return render(request, 'items/pp0102/practices_list.html', context)


def pp0102_New_practice(request):
    item = Items.objects.get(name="ПП.01.02. Прикладное программирование")
    form = PracticeForm()
    error = ""
    if request.method == "POST":
        form = PracticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0102_lectures'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "items/pp0102/forms/practice_new.html", {"form": form, "error": error, "item": item})


def download_lecture(request, pk):
    obj = Lectures.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


class UsersListView(ListView):
    """Список студентов"""
    model = Users
    queryset = Users.objects.all()
    template_name = 'users/users_list.html'


def download_practices(request, pk):
    obj = Practices.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


def calendar_form(request):
    form = CalendarForm()

    context = {"form": form}
    return render(request, 'calendar/calendar.html', context)
