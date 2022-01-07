from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('people/<str:pk>.html', views.person, name="person"),
    path('events.html', views.events, name="events"),

    path('books.html', views.books, name="books"),
    path('book/<str:pk>.html', views.book, name="book"),

    path('podcast.html', views.podcast, name="podcast"),
    path('podcast/<str:pk>.html', views.episode, name="episode"),
    path('blog.html', views.blog, name="blog"),
    path('blog/<str:pk>.html', views.post, name="post"),
]