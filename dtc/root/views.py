from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Event


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def person(request, pk):
    person = Person.objects.get(id=pk)
    events = person.event_set.all()
    context = {"person": person, "events": events}
    return render(request, 'root/person.html', context)


def events(request):
    events = Event.objects.all()

    now = timezone.now()
    upcoming_events = []
    past_events = []

    for event in events:
        if now > event.time:
            past_events.append(event)
        else:
            upcoming_events.append(event)

    context = {
        "past_events": past_events, 
        "upcoming_events": upcoming_events
    }

    return render(request, 'root/events.html', context)

