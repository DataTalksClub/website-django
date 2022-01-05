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
