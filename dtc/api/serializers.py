from rest_framework import serializers
from root.models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'



    
class EventSerializer(serializers.ModelSerializer):
    # speakers = PersonSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
        
        
class PodcastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Podcast
        fields = '__all__'
        
        
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        
        
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'
        
        
class SpecialPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpecialPost
        fields = '__all__'
        

class ToolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tool
        fields = '__all__'
        
        
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'
        

class SponsorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sponsor
        fields = '__all__'
        
        