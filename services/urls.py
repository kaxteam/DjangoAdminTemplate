from django.conf.urls import include, url
from rest_framework import routers
from services.views import RaspViewSet


router = routers.DefaultRouter()
router.register(r'rasp', RaspViewSet, base_name= 'api-rasp')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]