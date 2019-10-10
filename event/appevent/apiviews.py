
from rest_framework import viewsets,filters
# from drf_dynamic_fields import DynamicSearchFilter
# from rest_framework_api_key.permissions import HasAPIKey

from .models import *
from .serializers import *

# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])


class CompagnieViewset(viewsets.ModelViewSet):
    # filter_backends = (DynamicSearchFilter,)
    queryset = Compagnie.objects.all()
    serializer_class = CompagnieSerializer
    # permission_classes = [HasAPIKey]

class Categorie_eventViewset(viewsets.ModelViewSet):
    queryset = Categorie_event.objects.all()
    serializer_class = Categorie_eventSerializer
    # permission_classes = [HasAPIKey]

class CommuneViewset(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    # permission_classes = [HasAPIKey]

class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    # permission_classes = [HasAPIKey]

class ParticipantsViewset(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer
    # permission_classes = [HasAPIKey]

class Image_eventViewset(viewsets.ModelViewSet):
    queryset = Image_event.objects.all()
    serializer_class = Image_eventSerializer
    # permission_classes = [HasAPIKey]
