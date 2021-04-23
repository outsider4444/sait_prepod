from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse, Http404, FileResponse
import locale
from datetime import date, timedelta, datetime

from .forms import *
from .models import *


# Текущий месяц и его даты
def days_cur_month(strdate):
    locale.setlocale(locale.LC_ALL, "")
    m = datetime.now().month
    y = datetime.now().year
    ndays = (date(y, m + 1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1

    return [(d1 + timedelta(days=i)).strftime(strdate) for i in range(delta.days + 1)]


def registerPage(request):
    """Регистрация"""
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('name')
                usersurname = form.cleaned_data.get('surname')
                messages.success(request, 'Пользователь ' + username + '' + usersurname + ' был создан')
                return redirect('login')
        context = {"form": form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    """Авторизация"""
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Почта ИЛИ пароль не верны')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def main(request):
    users = UserProfile.objects.all()
    context = {"users": users}
    return render(request, 'main/main.html', context)


# ТРПО

# Лекции
@login_required(login_url='login')
def trpo_lecture(request):
    lectures = TrpoLectures.objects.filter(items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"lectures": lectures,}
    return render(request, 'items/trpo/lectures_list.html', context)


@login_required(login_url='login')
def trpo_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = TrpoLecturesForm()
    error = ""
    if request.method == "POST":
        form = TrpoLecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('trpo_lectures'))
        else:
            error = form.errors
    return render(request, "items/trpo/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
@login_required(login_url='login')
def trpo_practice(request):
    practice = TrpoPractices.objects.filter(items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"practice": practice,}
    return render(request, 'items/trpo/practices_list.html', context)


@login_required(login_url='login')
def trpo_New_practice(request):
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = TrpoPracticesForm()
    error = ""
    if request.method == "POST":
        form = TrpoPracticesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('trpo_practice'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "items/trpo/forms/practice_new.html", {"form": form, "error": error, "item": item})


# ПП.02.01

# Лекции
@login_required(login_url='login')
def pp0201_lecture(request):
    lectures = PP0201Lectures.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'items/pp0201/lectures_list.html', context)


@login_required(login_url='login')
def pp0201_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name='ПП.02.01. Прикладное программирование')
    form = Pp0201LecturesForm()
    error = ""
    if request.method == "POST":
        form = Pp0201LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0201_lectures'))
        else:
            error = form.errors
    return render(request, "items/pp0201/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
@login_required(login_url='login')
def pp0201_practice(request):
    practice = PP0201Practices.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"practice": practice,}
    return render(request, 'items/pp0201/practices_list.html', context)


@login_required(login_url='login')
def pp0201_New_practice(request):
    item = Items.objects.get(name='ПП.02.01. Прикладное программирование')
    form = Pp0201PracticesForm()
    error = ""
    if request.method == "POST":
        form = Pp0201PracticesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0201_lectures'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "items/pp0201/forms/practice_new.html", {"form": form, "error": error, "item": item})


# ПП.01.02

# Лекции
@login_required(login_url='login')
def pp0102_lecture(request):
    lectures = PP0102Lectures.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'items/pp0102/lectures_list.html', context)


@login_required(login_url='login')
def pp0102_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name="ПП.01.02. Прикладное программирование")
    form = Pp0102LecturesForm()
    error = ""
    if request.method == "POST":
        form = Pp0102LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0102_lectures'))
        else:
            error = form.errors
    return render(request, "items/pp0102/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
@login_required(login_url='login')
def pp0102_practice(request):
    practice = PP0102Practices.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"practice": practice,}
    return render(request, 'items/pp0102/practices_list.html', context)


@login_required(login_url='login')
def pp0102_New_practice(request):
    item = Items.objects.get(name="ПП.01.02. Прикладное программирование")
    form = Pp0102LecturesForm()
    error = ""
    if request.method == "POST":
        form = Pp0102LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('pp0102_lectures'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "items/pp0102/forms/practice_new.html", {"form": form, "error": error, "item": item})


@login_required(login_url='login')
def trpo_download_lecture(request, pk):
    obj = TrpoLectures.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


@login_required(login_url='login')
def trpo_download_practice(request, pk):
    obj = TrpoPractices.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


@login_required(login_url='login')
def pp0201_download_lecture(request, pk):
    obj = PP0201Lectures.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


@login_required(login_url='login')
def pp0201_download_practice(request, pk):
    obj = PP0201Practices.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


@login_required(login_url='login')
def pp0102_download_lecture(request, pk):
    obj = PP0102Lectures.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


@login_required(login_url='login')
def pp0102_download_practice(request, pk):
    obj = PP0102Practices.objects.get(id=pk)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


@login_required(login_url='login')
def trpo_users_marks_list(request):
    """Оценки за ТРПО"""
    marks = Marks.objects.filter(items_code__name='МДК.02.01. Технология разработки программного обеспечения')
    students = UserProfile.objects.all().distinct()
    # получение всех дат текущего месяца
    delta_date = days_cur_month(strdate='%d %B %Yг.')
    # месяц
    date_month = datetime.today().month
    # год
    date_year = datetime.today().year
    # дни
    date_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31]

    while date_days.__len__() != days_cur_month(strdate='%d %B %Yг.').__len__():
        del date_days[-1]

    marks.filter(
        Q(date__month=date_month) &
        Q(date__year=date_year)
    ).order_by('date').distinct()

    context = {"marks": marks, "students": students, "date_days": date_days, "delta_date": delta_date, "date_days ": date_days}
    return render(request, 'marks/trpo_marks_list.html', context)


def pp0201_users_marks_list(request):
    """Оценки за ПП0201"""
    marks = Marks.objects.all()

    context = {"marks": marks, }
    return render(request, '', context)


def pp0102_users_marks_list(request):
    """Оценки за ПП0102"""
    marks = Marks.objects.all()


    context = {"marks": marks, }
    return render(request, '', context)


