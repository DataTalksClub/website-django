from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('people/<str:pk>.html', views.person, name="person"),
    path('events.html', views.events, name="events"),
    path('books.html', views.books, name="books")
]