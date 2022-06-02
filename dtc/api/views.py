
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
        serializer = BookSerializer(book, data=request.data, partial=True)
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
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######## Tag views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def tags(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def tagDetails(request, pk):
    try:
        tag = Tag.objects.get(id=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = TagSerializer(tag, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = TagSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######## Special post  views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def specialPosts(request):
    if request.method == 'GET':
        specialPosts = SpecialPost.objects.all()
        serializer = SpecialPostSerializer(specialPosts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SpecialPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def specialPostDetails(request, pk):
    try:
        specialPost = SpecialPost.objects.get(id=pk)
    except SpecialPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = SpecialPostSerializer(specialPost, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SpecialPostSerializer(specialPost, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        specialPost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########  Tool views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def tools(request):
    if request.method == 'GET':
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def toolDetails(request, pk):
    try:
        tool = Tool.objects.get(id=pk)
    except Tool.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = ToolSerializer(tool, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = ToolSerializer(tool, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
########  Course views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def courseDetails(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = CourseSerializer(course, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
########  Sponsor views ########   
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def sponsors(request):
    if request.method == 'GET':
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(tools, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'DELETE', 'PATCH'])
def sponsorDetails(request, pk):
    try:
        sponsor = Sponsor.objects.get(id=pk)
    except Sponsor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = SponsorSerializer(sponsor, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SponsorSerializer(sponsor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        sponsor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

    
    









