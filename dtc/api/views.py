
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from root.models import *
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

######## People views ########
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def people(request):
    if request.method == 'GET':
        print("DATA+++++>:", request.data)
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

@api_view(['GET', 'DELETE', 'PATCH'])
def personDetails(request, pk):
    
    try:
        person = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

######## Events views ########
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

@api_view(['GET', 'DELETE', 'PATCH'])
def eventDetails(request, pk):
    try:
        event = Event.objects.get(id=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
######## Books views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def bookDetails(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = EventSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
######## podcast views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def podcast(request):
    if request.method == 'GET':
        podcast = Podcast.objects.all()
        serializer = PodcastSerializer(podcast, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PodcastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def episodeDetails(request, pk):
    try:
        episode = Podcast.objects.get(id=pk)
    except Podcast.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = PodcastSerializer(episode, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = PodcastSerializer(episode, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        episode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######## Blog views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def blog(request):
    if request.method == 'GET':
        blog = Post.objects.all()
        serializer = PostSerializer(blog, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def postDetails(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = EventSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








