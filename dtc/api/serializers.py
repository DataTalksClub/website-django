from rest_framework import serializers
from root.models import Person, Event

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    speakers = PersonSerializer(many=True)
    class Meta:
        model = Event
        fields = '__all__'