from django.urls import path

from .views import index, contact, check_for_past_event, classes, about

urlpatterns = [
    path("", index, name="index"),
    path("kontakt/", contact, name="contact"),
    path("wydarzenia/", check_for_past_event, name="events"),
    path("zajecia/", classes, name="classes"),
    path("o-mnie/", about, name="about"),
]
