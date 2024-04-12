from django.shortcuts import render
from .models import Event


def home(view):
    events = Event.objects.filter(display=True)
    return render(view, "home.html", {'events': events})


def event_detail(view, url):
    event = Event.objects.get(url=url)
    return render(view, "event_detail.html", {'event': event})

def events(view):
    return render(view, "events.html")


def galerie(view):
    return render(view, "galerie.html")




def history(view):
    return render(view, "history.html")

# Create your views here.
