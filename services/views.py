from rest_framework import viewsets
from rest_framework import mixins

from services.models import SampleModel
from services.serializers import SampleModelSerializer


class SampleViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
