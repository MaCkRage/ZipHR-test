from rest_framework.serializers import ModelSerializer

from plane.models import Plane


class PlaneSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plane
