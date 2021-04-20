from django.shortcuts import render
from .models import *


# Create your views here.

def main(request):
    return render(request, 'main/main.html',)


def lectures_list(request):
    lecture = Lectures.objects.all()
    return render(request, 'lectures/lectures_list.html', {"lecture": lecture})


def practices_list(request):
    practice = Practices.objects.all()
    return render(request, 'practice/practices_list.html', {"practice": practice})
