from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from .models import *

class ParticipantsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'


class EventsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    participant_event = ParticipantsSerializer(many=True, required=False)
    class Meta:
        model = Events
        fields = '__all__'


class CommuneSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    event_commune = EventsSerializer(many=True, required=False)

    class Meta:
        model = Commune
        fields = '__all__'



class Categorie_eventSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    event_categorie = EventsSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Categorie_event
        fields = '__all__'



class CompagnieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    event_compagnie = EventsSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Compagnie
        fields = '__all__'