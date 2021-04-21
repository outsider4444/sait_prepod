import os
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView

from .forms import CalendarForm
from .models import *


def main(request):
    return render(request, 'main/main.html',)


def trpo(request):
    return render(request, 'items/base.html',)


def pp0201(request):
    return render(request, 'items/base.html',)


def pp0102(request):
    return render(request, 'items/base.html',)


class LecturesListView(ListView):
    """Список лекций"""
    model = Lectures
    queryset = Lectures.objects.all()
    template_name = 'lectures/lectures_list.html'


def download_lecture(request, pk):
    obj = Lectures.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


class PracticesListView(ListView):
    """Список практик"""
    model = Practices
    queryset = Practices.objects.all()
    template_name = 'practice/practices_list.html'


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
