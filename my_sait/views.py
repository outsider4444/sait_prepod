from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.http import FileResponse
import locale
from datetime import date, timedelta, datetime

from .decorators import unauthenticated_user, allowed_users, admin_only
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
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='student')
            user.groups.add(group)

            username = form.cleaned_data.get('name')
            usersurname = form.cleaned_data.get('surname')
            messages.success(request, 'Пользователь ' + username + '' + usersurname + ' был создан')

            return redirect('login')

    context = {"form": form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    """Авторизация"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-main_page')
        else:
            messages.info(request, 'Почта ИЛИ пароль не верны')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# ДЛЯ АДМИНИСТРАТОРА


@login_required(login_url='login')
@admin_only
def admin_main_page(request):
    users = UserProfile.objects.all()
    context = {"users": users}
    return render(request, 'main/main.html', context)


# ТРПО

# Лекции
@login_required(login_url='login')
def admin_trpo_lecture(request):
    lectures = TrpoLectures.objects.filter(items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"lectures": lectures, }
    return render(request, 'admin-items/trpo/lectures_list.html', context)


@login_required(login_url='login')
def admin_trpo_New_lecture(request):
    # lecture_list = Lectures.objects.all()
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = TrpoLecturesForm()
    error = ""
    if request.method == "POST":
        form = TrpoLecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-trpo_lectures'))
        else:
            error = form.errors
    return render(request, "admin-items/trpo/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
@login_required(login_url='login')
def admin_trpo_practice(request):
    practice = TrpoPractices.objects.filter(
        items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"practice": practice, }
    return render(request, 'admin-items/trpo/practices_list.html', context)


@login_required(login_url='login')
def admin_trpo_New_practice(request):
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = TrpoPracticesForm()
    error = ""
    if request.method == "POST":
        form = TrpoPracticesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-trpo-practice'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "admin-items/trpo/forms/practice_new.html", {"form": form, "error": error, "item": item})


# ПП.02.01

# Лекции
@login_required(login_url='login')
def admin_pp0201_lecture(request):
    lectures = PP0201Lectures.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'admin-items/pp0201/lectures_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0201_New_lecture(request):
    item = Items.objects.get(name='ПП.02.01. Прикладное программирование')
    form = Pp0201LecturesForm()
    error = ""
    if request.method == "POST":
        form = Pp0201LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0201-lecture'))
        else:
            error = form.errors
    return render(request, "admin-items/pp0201/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
@login_required(login_url='login')
def admin_pp0201_practice(request):
    practice = PP0201Practices.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"practice": practice, }
    return render(request, 'admin-items/pp0201/practices_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0201_New_practice(request):
    item = Items.objects.get(name='ПП.02.01. Прикладное программирование')
    form = Pp0201PracticesForm()
    error = ""
    if request.method == "POST":
        form = Pp0201PracticesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0201-lecture'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "admin-items/pp0201/forms/practice_new.html", {"form": form, "error": error, "item": item})


# ПП.01.02

# Лекции
@login_required(login_url='login')
def admin_pp0102_lecture(request):
    lectures = PP0102Lectures.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'admin-items/pp0102/lectures_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0102_New_lecture(request):
    item = Items.objects.get(name="ПП.01.02. Прикладное программирование")
    form = Pp0102LecturesForm()
    error = ""
    if request.method == "POST":
        form = Pp0102LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0102-lecture'))
        else:
            error = form.errors
    return render(request, "admin-items/pp0102/forms/lecture_new.html", {"form": form, "error": error, "item": item})


# Практики
@login_required(login_url='login')
def admin_pp0102_practice(request):
    practice = PP0102Practices.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"practice": practice, }
    return render(request, 'admin-items/pp0102/practices_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0102_New_practice(request):
    item = Items.objects.get(name="ПП.01.02. Прикладное программирование")
    form = Pp0102LecturesForm()
    error = ""
    if request.method == "POST":
        form = Pp0102LecturesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0102-lecture'))
        else:
            error = "Форма неверно заполнена"
    return render(request, "admin-items/pp0102/forms/practice_new.html", {"form": form, "error": error, "item": item})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_trpo_marks_list(request):
    """Оценки за ТРПО"""
    marks = Marks.objects.filter(items_code__name='МДК.02.01. Технология разработки программного обеспечения')
    students = UserProfile.objects.filter(groups=2)
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

    context = {"marks": marks, "students": students, "date_days": date_days, "delta_date": delta_date,
               "date_days ": date_days}
    return render(request, 'admin-items/trpo/marks/trpo_marks_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_trpo_marks_create(request):
    item = Items.objects.get(name='МДК.02.01. Технология разработки программного обеспечения')
    form = CreateMarksForm()
    error = ""
    if request.method == "POST":
        form = CreateMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0201_students_marks'))
        else:
            error = form.errors
    return render(request, "admin-items/trpo/marks/forms/trpo_new_mark.html",
                  {"form": form, "error": error, 'item': item})


# AJAX
def load_group(request):
    id_group = request.GET.get('id_group')
    student_list = UserProfile.objects.filter(group__code=id_group).all()

    return render(request, 'admin-items/trpo/marks/forms/student_dropdown_list_options.html', {'student_list': student_list})


# ПП0201
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0201_marks_list(request):
    """Оценки за ПП0201"""
    marks = Marks.objects.filter(items_code__name='ПП.02.01. Прикладное программирование')
    students = UserProfile.objects.filter(groups=2)
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

    context = {"marks": marks, "students": students, "date_days": date_days, "delta_date": delta_date,
               "date_days ": date_days}
    return render(request, 'admin-items/pp0201/marks/pp0201_marks_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0201_marks_create(request):
    item = Items.objects.get(name='ПП.01.02. Прикладное программирование')
    form = CreateMarksForm()
    error = ""
    if request.method == "POST":
        form = CreateMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0201_students_marks'))
        else:
            error = form.errors
    return render(request, "admin-items/pp0201/marks/forms/pp0201_new_mark.html",
                  {"form": form, "error": error, 'item': item})


# ПП0102
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0102_marks_list(request):
    """Оценки за ПП0102"""
    marks = Marks.objects.filter(items_code__name='ПП.01.02. Прикладное программирование')
    students = UserProfile.objects.filter(groups=2)
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

    context = {"marks": marks, "students": students, "date_days": date_days, "delta_date": delta_date,
               "date_days ": date_days}
    return render(request, 'admin-items/pp0102/marks/pp0102_marks_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin_pp0102_marks_create(request):
    item = Items.objects.get(name='ПП.01.02. Прикладное программирование')
    form = CreateMarksForm()
    error = ""
    if request.method == "POST":
        form = CreateMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin-pp0102_students_marks'))
        else:
            error = form.errors
    return render(request, "admin-items/pp0102/marks/forms/pp0102_new_mark.html",
                  {"form": form, "error": error, 'item': item})


# ДЛЯ СТУДЕНТА


# Страничка студента

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):
    user = request.user
    user = UserProfile.objects.get(email=user.email)
    context = {"user": user}
    return render(request, 'accounts/student/student_main_page.html', context)


# ТРПО

# Лекции
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_trpo_lecture(request):

    lectures = TrpoLectures.objects.filter(items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"lectures": lectures, }
    return render(request, 'accounts/student/items/trpo/lectures_list.html', context)


# Практики
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_trpo_practice(request):
    practice = PP0102Practices.objects.filter(
        items_code__name="МДК.02.01. Технология разработки программного обеспечения")
    context = {"practice": practice, }
    return render(request, 'admin-items/pp0102/practices_list.html', context)


# Оценки
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_trpo_marks_list(request):
    user = UserProfile.objects.get(email=request.user.email)
    marks = Marks.objects.filter(
        Q(items_code__name='МДК.02.01. Технология разработки программного обеспечения') &
        Q(users_code=user)
    )
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

    context = {"marks": marks, "user": user, "date_days": date_days, "delta_date": delta_date,
               "date_days ": date_days}
    return render(request, 'accounts/student/items/trpo/marks/marks_list.html', context)


# ПП.02.01

# Лекции
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_pp0201_lecture(request):
    lectures = PP0201Lectures.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'accounts/student/items/pp0201/lectures_list.html', context)


# Практики
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_pp0201_practice(request):
    practice = PP0102Practices.objects.filter(items_code__name="ПП.02.01. Прикладное программирование")
    context = {"practice": practice, }
    return render(request, 'admin-items/pp0102/practices_list.html', context)


# Оценки
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_pp0201_marks_list(request):
    user = UserProfile.objects.get(email=request.user.email)
    marks = Marks.objects.filter(
        Q(items_code__name='ПП.02.01. Прикладное программирование') &
        Q(users_code=user)
    )
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

    context = {"marks": marks, "user": user, "date_days": date_days, "delta_date": delta_date,
               "date_days ": date_days}
    return render(request, 'accounts/student/items/pp0201/marks/marks_list.html', context)


# ПП.01.02

# Лекции
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_pp0102_lecture(request):
    lectures = PP0102Lectures.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"lectures": lectures, }
    return render(request, 'accounts/student/items/pp0102/lectures_list.html', context)


# Практики
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_pp0102_practice(request):
    practice = PP0102Practices.objects.filter(items_code__name="ПП.01.02. Прикладное программирование")
    context = {"practice": practice, }
    return render(request, 'admin-items/pp0102/practices_list.html', context)


# Оценки
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_pp0102_marks_list(request):
    user = UserProfile.objects.get(email=request.user.email)
    marks = Marks.objects.filter(
        Q(items_code__name='ПП.01.02. Прикладное программирование') &
        Q(users_code=user)
    )
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

    context = {"marks": marks, "user": user, "date_days": date_days, "delta_date": delta_date,
               "date_days ": date_days}
    return render(request, 'accounts/student/items/pp0102/marks/marks_list.html', context)


# ОБЩЕЕ
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
