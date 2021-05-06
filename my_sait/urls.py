from django.urls import path, include

from . import views

urlpatterns = [
    # Оценки студентов
    path('user/trpo_lectures_list/marks', views.user_trpo_marks_list, name="user-trpo-marks"),
    path('user/pp0201_lectures_list/marks', views.user_pp0201_marks_list, name="user-pp0201-marks"),
    path('user/pp0102_lectures_list/marks', views.user_pp0102_marks_list, name="user-pp0102-marks"),

    # Скачать лекцию/практику студенту
    path('user/trpo_lectures_list/<int:pk>', views.trpo_download_lecture, name="user-trpo_lectures_download"),
    path('user/trpo_practices_list/<int:pk>', views.trpo_download_practice, name="user-trpo_practice_download"),
    path('user/pp0201_lectures_list/<int:pk>', views.pp0201_download_lecture, name="user-pp0201_lectures_download"),
    path('user/pp0201_practices_list/<int:pk>', views.pp0201_download_practice, name="user-pp0201_practice_download"),
    path('user/pp0102_lectures_list/<int:pk>', views.pp0102_download_lecture, name="user-pp0102_lectures_download"),
    path('user/pp0102_practices_list/<int:pk>', views.pp0102_download_practice, name="user-pp0102_practice_download"),

    # Скачать лекцию/практику преподу
    path('trpo_lectures_list/<int:pk>', views.trpo_download_lecture, name="admin-trpo_lectures_download"),
    path('trpo_practices_list/<int:pk>', views.trpo_download_practice, name="admin-trpo_practice_download"),
    path('pp0201_lectures_list/<int:pk>', views.pp0201_download_lecture, name="admin-pp0201_lectures_download"),
    path('pp0201_practices_list/<int:pk>', views.pp0201_download_practice, name="admin-pp0201_practice_download"),
    path('pp0102_lectures_list/<int:pk>', views.pp0102_download_lecture, name="admin-pp0102_lectures_download"),
    path('pp0102_practices_list/<int:pk>', views.pp0102_download_practice, name="admin-pp0102_practice_download"),

    # Создание новой лекции
    path('trpo_lectures_list/trpo_new_lecture', views.admin_trpo_New_lecture, name="admin-trpo_new_lecture"),
    path('trpo_practices_list/trpo_new_lecture', views.admin_pp0201_New_lecture, name="admin-pp0201_new_lecture"),
    path('pp0201_practices_list/trpo_new_lecture', views.admin_pp0102_New_lecture, name="admin-pp0102_new_lecture"),
    # Создание новой практики
    path('trpo_practices_list/trpo_new_practice', views.admin_trpo_New_practice, name="admin-trpo_new_practice"),
    path('pp0201_lectures_list/trpo_new_practice', views.admin_pp0201_New_practice, name="admin-pp0201_new_practice"),
    path('pp0102_lectures_list/trpo_new_practice', views.admin_pp0102_New_practice, name="admin-pp0102_new_practice"),


    # Создание новой оценки по ТРПО
    path('trpo/students_marks/create_new_marks', views.admin_trpo_marks_create, name="admin-trpo_students_marks_create"),
    # Создание новой оценки по ПП0201
    path('pp0201/students_marks/create_new_marks', views.admin_pp0201_marks_create, name="admin-pp0201_students_marks_create"),
    # Создание новой оценки по ПП0102
    path('pp0102/students_marks/create_new_marks', views.admin_pp0102_marks_create, name="admin-pp0102_students_marks_create"),


    # Оценки для админа по ТРПО
    path('trpo/students_marks/', views.admin_trpo_marks_list, name="admin-trpo_students_marks"),
    # ПП0201
    path('pp0201/students_marks/', views.admin_pp0201_marks_list, name="admin-pp0201_students_marks"),
    # ПП0102
    path('pp0102/students_marks/', views.admin_pp0102_marks_list, name="admin-pp0102_students_marks"),

    # Список практик для студента
    path('user/trpo_practices_list/', views.user_trpo_practice, name="user-trpo_practice"),
    path('user/pp0201_practices_list/', views.user_pp0201_practice, name="user-pp0201-practice"),
    path('user/pp0102_practices_list/', views.user_pp0102_practice, name="user-pp0102-practice"),

    # Список практик для админа
    path('trpo_practices_list/', views.admin_trpo_practice, name="admin-trpo-practice"),
    path('pp0201_practices_list/', views.admin_pp0201_practice, name="admin-pp0201-practice"),
    path('pp0102_practices_list/', views.admin_pp0102_practice, name="admin-pp0102-practice"),

    # Список лекций для студента
    path('user/trpo_lectures_list', views.user_trpo_lecture, name='user-trpo-lecture'),
    path('user/pp0201_lectures_list', views.user_pp0201_lecture, name='user-pp0201-lecture'),
    path('user/pp0102_lectures_list', views.user_pp0102_lecture, name='user-pp0102-lecture'),

    # список лекций для админа
    path('trpo_lectures_list/', views.admin_trpo_lecture, name="admin-trpo-lecture"),
    path('pp0201_lectures_list/', views.admin_pp0201_lecture, name="admin-pp0201-lecture"),
    path('pp0102_lectures_list/', views.admin_pp0102_lecture, name="admin-pp0102-lecture"),

    path('user/', views.userPage, name='user-page'),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path("", views.admin_main_page, name="admin-main_page"),
]