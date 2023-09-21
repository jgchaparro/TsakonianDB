from django.urls import path

from . import views

app_name = "dictionary"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>/", views.entry, name="entry"),
]