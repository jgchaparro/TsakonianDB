from django.urls import path

from . import views

app_name = "dictionary"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("TS-EL/<str:entry>", views.tsakonian, name="tsakonian-greek"),
    path("EL-TS/<str:entry>", views.greek, name="greek-tsakonian"),
]