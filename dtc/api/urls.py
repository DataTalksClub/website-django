from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.getRoutes),
    # path('obtain-token/', obtain_auth_token),
    
    path('people/', views.people),
    path('people/<str:pk>/', views.personDetails),
    
    path('events/', views.events),
    path('events/<str:pk>/', views.eventDetails),
    
    path('books/', views.books),
    path('books/<str:pk>/', views.bookDetails),
    
    path('podcast/', views.podcast),
    path('podcast/<str:pk>/', views.episodeDetails),
    
    path('blog/', views.blog),
    path('blog/<str:pk>/', views.postDetails),
    
    path('tags/', views.tags),
    path('tags/<str:pk>/', views.tagDetails),
    
    path('special-posts/', views.specialPosts),
    path('special-posts/<str:pk>/', views.specialPostDetails),
    
    path('tools/', views.tools),
    path('tools/<str:pk>/', views.toolDetails),
    
    path('courses/', views.courses),
    path('courses/<str:pk>/', views.courseDetails),
    
    path('sponsors/', views.sponsors),
    path('sponsors/<str:pk>/', views.sponsorDetails),
]
