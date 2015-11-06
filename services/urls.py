from django.conf.urls import include, url
from rest_framework import routers
from services.views import SampleViewSet

router = routers.DefaultRouter()
router.register('samples', SampleViewSet, base_name= 'api-sample')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]