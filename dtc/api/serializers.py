from rest_framework import serializers
from root.models import Person, Event, Book

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