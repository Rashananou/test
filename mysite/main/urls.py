from django.urls import path
from . import views

urlpatterns=[
path("",views.index,name="index"),
path("Home",views.index,name="home"),
path("gallery",views.gallery,name="gallery"),
path("addcar",views.addcar,name="addcar"),
path("about",views.about,name="about"),
]