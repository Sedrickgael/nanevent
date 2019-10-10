
from rest_framework import viewsets,filters
# from drf_dynamic_fields import DynamicSearchFilter

from .models import *
from .serializers import *

# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])


class CompagnieViewset(viewsets.ModelViewSet):
    # filter_backends = (DynamicSearchFilter,)
    queryset = Compagnie.objects.all()
    serializer_class = CompagnieSerializer

class Categorie_eventViewset(viewsets.ModelViewSet):
    queryset = Categorie_event.objects.all()
    serializer_class = Categorie_eventSerializer

class CommuneViewset(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer

class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class ParticipantsViewset(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = EventsSerializer

class Image_eventViewset(viewsets.ModelViewSet):
    queryset = Image_event.objects.all()
    serializer_class = EventsSerializer
