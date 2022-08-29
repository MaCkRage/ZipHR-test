from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from plane.models import Plane
from plane.serializers import PlaneSerializer

# from drf_spectacular.utils import extend_schema, extend_schema_view

# @extend_schema_view(
#     create=extend_schema(responses={status.HTTP_201_CREATED: serializers.ProductSerializer,
#                                     status.HTTP_400_BAD_REQUEST: serializers.ValidationErrorSerializer, }),
#     update=extend_schema(responses={status.HTTP_201_CREATED: serializers.ProductSerializer,
#                                     status.HTTP_400_BAD_REQUEST: serializers.ValidationErrorSerializer, }))

class PlanetViewSet(ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = [
        # AllowAny,
    ]
    # serializer_class = serializers.ProductSerializer

    @action(detail=False, methods=['get'])
    def fuel_consumption(self, request):
        return Response(status=status.HTTP_200_OK)
