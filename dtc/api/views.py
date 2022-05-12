
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import PersonSerializer, EventSerializer
from root.models import Person, Event
from rest_framework import status


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
# @permission_classes([IsAuthenticated])
def getPeople(request):
    print("DATA+++++>:", request.data)
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def addPerson(request):
    print("DATA+++++>:", request.data)
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

@api_view(['GET', 'DELETE', 'PUT'])
def personDetails(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == 'GET':
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    
    # elif request.method == 'PUT':




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

