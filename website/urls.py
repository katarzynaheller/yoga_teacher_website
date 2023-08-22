from django.urls import path

from .views import index, contact, EventListView, classes, about

urlpatterns = [
    path("", index, name="index"),
    path("kontakt/", contact, name="contact"),
    path("wydarzenia/", EventListView.as_view(), name="events"),
    path("zajecia/", classes, name="classes"),
    path("o-mnie/", about, name="about"),
]
