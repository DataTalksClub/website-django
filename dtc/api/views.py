
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import PersonSerializer, EventSerializer
from root.models import Person, Event


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'api/people/'},
        {'GET':'api/people/id/'},
                       
        {'GET': 'api/events.html'},

        {'GET': 'api/books.html'},
        {'GET': 'api/book/<str:pk>.html'},

        {'GET': 'api/podcast.html'},
        {'GET': 'api/podcast/<str:pk>.html'},
        
        {'GET': 'api/blog.html'},
        {'GET': 'api/blog/<str:pk>.html'},

        {'GET': 'api/tools.html'},
        {'GET': 'api/tool/<str:pk>.html'},

        {'GET': 'api/courses.html'},
        {'GET': 'api/course/<str:pk>.html'},

        {'GET': 'api/sponsors.html'},

        {'GET': 'api/<path:pk>.html'},

        
        
    ]
    
    return Response(routes)

@api_view(['GET'])
def getPeople(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPerson(request, pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

