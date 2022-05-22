from rest_framework import serializers
from root.models import Person, Event

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    # def create(self, validated_data):
    #     raise NotImplementedError('`create()` must be implemented.')

    # def update(self, instance, validated_data):
    #     raise NotImplementedError('`update()` must be implemented.')
 
class EventSerializer(serializers.ModelSerializer):
    # speakers = PersonSerializer(many=True)
    class Meta:
        model = Event
        fields = '__all__'