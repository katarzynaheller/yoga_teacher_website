from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.utils import timezone

from website.models import Yoga_Retreat


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def contact(request):
    return render(request, "contact.html", {})


def classes(request):
    return render(request, "classes.html", {})


def about(request):
    return render(request, "about.html", {})


# class EventListView(ListView):
#     model = Yoga_Retreat
#     template_name = "events.html"
#     context_object_name = "events"


def check_for_past_event(request):
    events = Yoga_Retreat.objects.all().order_by("-from_date")
    today = timezone.now().date()

    for event in events:
        event.is_past = event.from_date < today

    return render(request, "events.html", {"events": events, "today": today})
