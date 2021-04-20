from django.urls import path, include

from . import views

urlpatterns = [

    path("lectures_list/", views.lectures_list, name="lectures_list"),
    path("practices_list/", views.practices_list, name="practices_list"),


    path('accounts/', include("allauth.urls")),
    path("", views.main),
]