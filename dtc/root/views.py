from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime


def index(request):
    now = datetime.datetime.today()
    events_set = Event.objects.filter(time__gte=now).order_by('time')[:2]
    podcast = Podcast.objects.all()[0]
    posts_set = Post.objects.all()[:2]
    books = Book.objects.filter(end_date__gte=now)
    if len(books) == 0:
        book = None
    else:
        book = books[0]
    print('LOOK HERE ===>', book)
    context = {"events": events_set, "podcast": podcast, "posts": posts_set, "book": book}
    return render(request, 'root/index1.html', context)

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

def books(request):
    books = Book.objects.all()

    today = timezone.now().date()
    upcoming_books = []
    past_books = []

    for book in books:
        if today > book.end_date:
            past_books.append(book)
        else:
            upcoming_books.append(book)

    context = {
        "past_books": past_books, 
        "upcoming_books": upcoming_books
    }

    return render(request, 'root/books.html', context)

def book(request, pk):
    book = Book.objects.get(id=pk)
    context = {"book": book}

    return render(request, 'root/book.html', context)

def podcast(request):
    episodes = Podcast.objects.all()
    episodes_grouped = {}
    for episode in episodes:
        season = episode.season
        if season not in episodes_grouped:
            episodes_grouped[season] = []
        episodes_grouped[season].append(episode)
    print(episodes_grouped)

    context = {"episodes": episodes_grouped}
    return render(request, 'root/podcast.html', context)


def episode(request, pk):
    episode = Podcast.objects.get(id=pk)
    context = {"episode": episode}

    return render(request, 'root/episode.html', context)

def blog(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'root/blog.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}

    return render(request, 'root/post.html', context)

def special_post(request, pk):
    post = SpecialPost.objects.get(id=pk)
    context = {"post": post}

    return render(request, 'root/post.html', context)

def tools(request):
    tools = Tool.objects.all()
    context = {"tools": tools}

    return render(request, 'root/tools.html', context)

def tool(request, pk):
    tool = Tool.objects.get(id=pk)
    context = {"tool": tool}

    return render(request, 'root/tool.html', context)

def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}

    return render(request, 'root/courses.html', context)

def course(request, pk):
    course = Course.objects.get(id=pk)
    context = {"course": course}

    return render(request, 'root/course.html', context)

def sponsors(request):
    sponsors = Sponsor.objects.all()
    context = {"sponsors": sponsors}

    return render(request, 'root/sponsors.html', context)






