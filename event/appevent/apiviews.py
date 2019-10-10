
from rest_framework import viewsets,filters

from .models import *
from .serializers import ParticipantsSerializer, EventsSerializer, CommuneSerializer, Categorie_eventSerializer, CompagnieSerializer

# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])


class CompagnieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Poll.objects.all()
    serializer_class = CompagnieSerializer

class Categorie_eventViewset(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = Categorie_eventSerializer

class CommuneViewset(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = CommuneSerializer

class EventsViewset(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = EventsSerializer
