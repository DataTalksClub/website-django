from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    
    path('people/', views.getPeople),
    path('people/<str:pk>', views.getPerson),
    
    path('events/', views.getEvents)
]
