from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def person(request, pk):
    person = Person.objects.get(id=pk)
    context = {"person": person}
    return render(request, 'root/person.html', context)
