from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.getRoutes),
    # path('obtain-token/', obtain_auth_token),
    
    path('people/', views.getPeople),
    path('people/add/', views.addPerson),
    path('people/<str:pk>/', views.personDetails),
    
    path('events/', views.getEvents),
    path('events/<str:pk>/', views.getEvent)
]
