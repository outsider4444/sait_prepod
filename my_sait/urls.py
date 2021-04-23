from django.urls import path, include

from . import views

urlpatterns = [
    # Скачать лекцию/практику
    path('trpo/<int:pk>', views.download_lecture, name="trpo_lectures_download"),
    path('trpo/practices_list/<int:pk>', views.download_practices, name="trpo_practice_download"),
    path('pp0201/<int:pk>', views.download_lecture, name="trpo_lectures_download"),
    path('pp0201/practices_list/<int:pk>', views.download_practices, name="trpo_practice_download"),
    path('pp0102/<int:pk>', views.download_lecture, name="trpo_lectures_download"),
    path('pp0102/practices_list/<int:pk>', views.download_practices, name="trpo_practice_download"),

    # Создание новой лекции
    path('trpo/trpo_new_lecture', views.trpo_New_lecture, name="trpo_new_lecture"),
    path('pp0201/trpo_new_lecture', views.pp0201_New_lecture, name="pp0201_new_lecture"),
    path('pp0102/trpo_new_lecture', views.pp0102_New_lecture, name="pp0102_new_lecture"),
    # Создание новой практики
    path('trpo/trpo_new_practice', views.trpo_New_practice, name="trpo_new_practice"),
    path('pp0201/trpo_new_practice', views.pp0201_New_practice, name="pp0201_new_practice"),
    path('pp0102/trpo_new_practice', views.pp0102_New_practice, name="pp0102_new_practice"),


    path('trpo/students_marks/', views.trpo_users_marks_list, name="trpo_students_marks"),

    # список практик
    path('trpo/trpo_pracrice', views.trpo_practice, name="trpo_practice"),
    path('pp0201/trpo_pracrice', views.pp0201_practice, name="pp0201_practice"),
    path('pp0102/trpo_pracrice', views.pp0102_practice, name="pp0102_practice"),

    # список лекций
    path('trpo/', views.trpo_lecture, name="trpo_lectures"),
    path('pp0201/', views.pp0201_lecture, name="pp0201_lecture"),
    path('pp0102/', views.pp0102_lecture, name="pp0102_lecture"),

    path('accounts/', include("allauth.urls")),
    path("", views.main, name="main"),
]