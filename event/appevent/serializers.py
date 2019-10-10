from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from .models import *



class EventsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class ParticipantsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    id_event = EventsSerializer(many=True, required=False)

    class Meta:
        model = Users
        fields = '__all__'

class CommuneSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    event_commune = EventsSerializer(many=True, required=False)

    class Meta:
        model = Commune
        fields = '__all__'

        

class Categorie_eventSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'



