from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

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


class EventListView(ListView):
    model = Yoga_Retreat
    template_name = "events.html"
    context_object_name = "events"
