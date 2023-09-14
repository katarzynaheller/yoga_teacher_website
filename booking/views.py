from datetime import date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import YogaClass, Booking


def monthly_classes(request):
    try:
        today = date.today()
        month_from_today = today + timedelta(days=30)
        classes = YogaClass.objects.filter(date__range=(today, month_from_today))

    except YogaClass.DoesNotExist:
        classes = None
        message = "Grafik dostępny wkrótce. Napisz na: info@jogagosiapardula.pl"

    return render(
        request,
        "monthly_classes.html",
        {"classes": classes, "message": message if classes is None else None},
    )


def book_class(request, class_id):
    yoga_class = get_object_or_404(YogaClass, id=class_id)

    if request.method == "POST":
        email = request.POST["email"]

        existing_booking = Booking.objects.filter(
            yoga_class=yoga_class, email=email
        ).first()

        if existing_booking:
            messages.warning(
                request,
                "Rezerwacja miejsca została juz wcześniej dokonana na te zajęcia, mozesz zarezerwować tylko jedno miejsce",
            )
            return redirect(reverse("list_bookings_by_email") + f"?email={email}")

        if yoga_class.slots > 0:
            new_booking = Booking(yoga_class=yoga_class, email=email)
            new_booking.save()

            yoga_class.slots -= 1
            yoga_class.save()

            messages.success(request, "Rezerwacja potwierdzona")

            return redirect(reverse("list_bookings_by_email") + f"?email={email}")
        else:
            return HttpResponse("Aktualnie brak miejsc")

    return render(request, "book_class.html", {"yoga_class": yoga_class})


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    yoga_class = booking.yoga_class
    email = booking.email
    yoga_class.slots += 1
    yoga_class.save()

    booking.delete()

    messages.success(request, "Rezerwacja anulowana")

    return redirect(reverse("list_bookings_by_email") + f"?email={email}")


def list_bookings_by_email(request):
    email_query = request.GET.get("email", "")
    bookings = Booking.objects.filter(email=email_query)
    return render(
        request,
        "my_classes.html",
        {"bookings": bookings, "email_query": email_query},
    )


# @login_required
# def book_class(request, class_id):
#     yoga_class = YogaClass.objects.get(id=class_id)

#     if yoga_class.slots > 0:
#         Booking.objects.create(yoga_class=yoga_class, user=request.user)
#         yoga_class.slots -= 1
#         yoga_class.save()

#         return render(request, "book_class.html")
#     else:
#         message = "Grafik dostępny wkrótce. Napisz na: info@jogagosiapardula.pl"


# @login_required
# def cancel_booking(request, booking_id):
#     booking = Booking.objects.get(id=booking_id, user=request.user)

#     if booking.status == "zapisano":
#         booking.status = "odwołano"
#         booking.yoga_class.slots += 1
#         booking.yoga_class.save()
#         booking.save()

#         return redirect("/")
