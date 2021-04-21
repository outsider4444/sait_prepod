from django.urls import path, include

from . import views

urlpatterns = [
    path("lectures_list/<int:pk>", views.download_lecture, name="lectures_download"),
    path("practices_list/<int:pk>", views.download_practices, name="practice_download"),

    # список лекций и практик
    path("lectures_list/", views.LecturesListView.as_view(), name="lectures_list"),
    path("practices_list/", views.PracticesListView.as_view(), name="practices_list"),
    path("users_list/", views.UsersListView.as_view(), name="users_list"),

    path("calendar_form/", views.calendar_form, name="calendar_form"),

    path('trpo/', views.trpo, name="trpo"),
    path('pp0201/', views.trpo, name="pp0201"),
    path('pp0102/', views.trpo, name="pp0102"),


    path('accounts/', include("allauth.urls")),
    path("", views.main, name="main"),
]