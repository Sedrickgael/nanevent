from rest_framework.routers import DefaultRouter

from .apiviews import *

router= DefaultRouter()
router.register('compagnieapi', CompagnieViewset, base_name='compagnieapi')
router.register('categorieapi', Categorie_eventViewset, base_name='categorieapi')
router.register('communeapi', CommuneViewset, base_name='communeapi')
router.register('eventapi', EventsViewset, base_name='eventapi')
router.register('participantapi', ParticipantsViewset, base_name='participantapi')

urlpatterns = [
    
]

urlpatterns += router.urls
