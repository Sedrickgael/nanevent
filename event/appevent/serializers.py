from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from .models import *


class EventsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class CommuneSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    votes = EventsSerializer(many=True, required=False)

    class Meta:
        model = Commune
        fields = '__all__'


class CompagnieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    votes = EventsSerializer(many=True, required=False)

    class Meta:
        model = Compagnie
        fields = '__all__'

        

class PollSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'