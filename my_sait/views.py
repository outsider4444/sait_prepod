import os
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from .models import *


# Create your views here.

def main(request):
    return render(request, 'main/main.html',)


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


def practices_list(request):
    practice = Practices.objects.all()
    return render(request, 'practice/practices_list.html', {"practice": practice})
