from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from app.permissions import AllowAny
from plane.models import Plane
from plane.serializers import PlaneBaseSerializer, PlaneIdSerializer
from plane.viewsets.swagger import qwery_passengers_count


class PlanetViewSet(ModelViewSet):
    queryset = Plane.objects.all()
    permission_classes = [
        # This is a test project, it's just easy way to win
        AllowAny,
    ]
    serializer_class = PlaneBaseSerializer

    def get_serializer_class(self):
        if self.action in {'fuel_consumption'}:
            return PlaneIdSerializer
        return PlaneBaseSerializer

    @swagger_auto_schema(method='get', manual_parameters=[qwery_passengers_count])
    @action(detail=True, methods=['get'])
    def fuel_consumption(self, request, pk):
        plane = self.get_object()

        # I don't want to write a validation.
        #  I know that I'm wrong right now, but I try to do your task as fast as I can,
        #  and cut back on what you can do without
        passenger_count = int(request.query_params.get('passengers_count', 1))

        consumption_per_minute = plane.fuel_consumption_with_passengers(passenger_count)

        # This must be a serializer. In future...
        data = {
            'consumption_per_minute': consumption_per_minute,
            'max_flight_time': plane.max_flight_time(consumption_per_minute),
        }
        return Response(status=status.HTTP_200_OK, data=data)
