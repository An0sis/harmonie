from django.shortcuts import render
from .models import Event, Picture, Contact
from django.utils import timezone


def home(view):
    event = Event.objects.filter(date__gte=timezone.now().date()).order_by('date')
    pictures = Picture.objects.filter(carrousel=True)
    return render(view, "home.html", {'events': event, 'pictures': pictures})


def event_detail(view, url):
    event = Event.objects.get(url=url)
    return render(view, "event_detail.html", {'event': event})


def events(view):
    future_events = Event.objects.filter(date__gte=timezone.now().date()).order_by('date')
    past_events = Event.objects.filter(date__lt=timezone.now().date()).order_by('-date')
    return render(view, "events.html", context={'future_events': future_events, 'past_events': past_events})


def galerie(view):
    return render(view, "galerie.html")


def history(view):
    return render(view, "history.html")


def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(nom=nom, prenom=prenom, email=email, message=message)
        contact.save()
    return render(request, "contact.html")

# Create your views here.
