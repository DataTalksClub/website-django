from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer, EventSerializer
from root.models import Person, Event


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'api/root/people/id.html'},
        {'GET':'api/root/people/id'},
                       
        {'GET': 'api/root/events.html'},

        {'GET': 'api/root/books.html'},
        {'GET': 'api/root/book/<str:pk>.html'},

        {'GET': 'api/root/podcast.html'},
        {'GET': 'api/root/podcast/<str:pk>.html'},
        
        {'GET': 'api/root/blog.html'},
        {'GET': 'api/root/blog/<str:pk>.html'},

        {'GET': 'api/root/tools.html'},
        {'GET': 'api/root/tool/<str:pk>.html'},

        {'GET': 'api/root/courses.html'},
        {'GET': 'api/root/course/<str:pk>.html'},

        {'GET': 'api/root/sponsors.html'},

        {'GET': 'api/root/<path:pk>.html'},

        
        
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