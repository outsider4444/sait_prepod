from django.urls import path, include

from . import views

urlpatterns = [

    path('trpo/<int:pk>', views.download_lecture, name="trpo_lectures_download"),
    # path('trpo/practices_list/<int:pk>', views.trpo_lecture, name="trpo_practice_download"),
    # path('pp0201/<int:pk>', views.trpo_lecture, name="pp0201"),
    # path('pp0201/practices_list/', views.trpo_lecture, name="pp0201"),
    # path('pp0102/<int:pk>', views.trpo_lecture, name="pp0102"),
    # path('pp0102/practices_list/<int:pk>', views.trpo_lecture, name="pp0102"),

    # список лекций и практик
    # path('trpo/practices_list', views.trpo_practice, name="trpo_practice"),
    # path('pp0201/practices_list', views.trpo_lecture, name="pp0201"),
    # path('pp0102/practices_list', views.trpo_lecture, name="pp0102"),


    # главная_переход_к_предмету
    path('trpo/', views.trpo_lecture, name="trpo_lectures"),
    path('pp0201/', views.trpo_lecture, name="pp0201"),
    path('pp0102/', views.trpo_lecture, name="pp0102"),


    path('accounts/', include("allauth.urls")),
    path("", views.main, name="main"),
]