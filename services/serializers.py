from rest_framework import serializers

from services.models import SampleModel


class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel