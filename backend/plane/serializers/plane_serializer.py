from rest_framework.serializers import ModelSerializer

from plane.models import Plane


class PlaneBaseSerializer(ModelSerializer):
    class Meta:
        # I know this is a bad practice, in real life I never use this
        fields = '__all__'
        model = Plane


class PlaneIdSerializer(ModelSerializer):
    class Meta:
        model = Plane
        fields = ('id', )
