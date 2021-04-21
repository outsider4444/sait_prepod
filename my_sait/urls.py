from django.urls import path, include

from . import views

urlpatterns = [
    path("lectures_list/<int:pk>", views.download_lecture, name="lectures_download"),
    path("practices_list/<int:pk>", views.practices_list, name="lectures_download"),

    # список лекций и практик
    path("lectures_list/", views.LecturesListView.as_view(), name="lectures_list"),
    path("practices_list/", views.practices_list, name="practices_list"),


    path('accounts/', include("allauth.urls")),
    path("", views.main),
]