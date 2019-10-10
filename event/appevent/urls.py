from rest_framwork.routers import DefaultRouter

from .apiviews import *

router= DefaultRouter()
router.register('compagnieapi', CompagnieViewSet, base_name='compagnieapi')
router.register('categorieapi', Categorie_eventViewset, base_name='categorieapi')
router.register('communeapi', CommuneViewset, base_name='communeapi')
router.register('eventapi', EventsViewset, base_name='eventapi')

urlpatterns = [
    
]

urlpatterns += router.urls
