from django.urls import path
from . import views

urlpatterns = [
    path("", views.monthly_classes, name="monthly_classes"),
    path("zapis/<int:class_id>/", views.book_class, name="book_class"),
    path("moje-zapisy/", views.list_bookings_by_email, name="list_bookings_by_email"),
    path("anulowanie/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]
