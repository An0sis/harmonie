from django.shortcuts import render
from .models import Event, Picture, Contact, Collection
from django.utils import timezone
from django.core.mail import send_mail


def home(view):
    event = Event.objects.filter(date__gte=timezone.now().date()).order_by('date')
    return render(view, "home.html", {'events': event})


def event_detail(view, url):
    event = Event.objects.get(url=url)
    return render(view, "event_detail.html", {'event': event})


def events(view):
    future_events = Event.objects.filter(date__gte=timezone.now().date()).order_by('date')
    past_events = Event.objects.filter(date__lt=timezone.now().date()).order_by('-date')
    return render(view, "events.html", context={'future_events': future_events, 'past_events': past_events})


def galerie(view):
    collections_picture = []
    collections = Collection.objects.all()

    for collection in collections:
        pictures = Picture.objects.filter(collection=collection)
        collections_picture.append((collection, pictures))

    return render(view, "galerie.html", {"collections": collections_picture})


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
        send_mail(
            'Nouveau message de contact',
            f"Nom: {nom}\nPrénom: {prenom}\nEmail: {email}\nMessage: {message}",
            'hantzberg.joric@gmail.com',
            ['harmonie.obenheim@gmail.com'])
    return render(request, "contact.html")


# Create your views here.
def galerie_collection(request, url):
    collection = Collection.objects.get(url=url)
    pictures = Picture.objects.filter(collection=collection)
    return render(request, "galerie_collection.html", {'collection': collection, 'pictures': pictures})
