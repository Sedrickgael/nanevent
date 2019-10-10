from rest_framwork.routers import DefaultRouter

from .viewsets import *

router= DefaultRouter()
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')
router.register('compagnieapi', BannerCompagnieViewSet, base_name='compagnieapi')

urlpatterns = [
    
]

urlpatterns += router.urls
