from plane.models import Plane

from django.test import TestCase


class PlaneTestCase(TestCase):
    fixtures = ['plane_plane']

    def setUp(self) -> None:
        self.plane = Plane.objects.get(pk=100500)

    def test_fuel_tank_capacity(self):
        self.assertEqual(20100000, self.plane.fuel_tank_capacity)

    def test_fuel_consumption_with_passengers(self):
        passengers_count = 100
        fuel_consumption_with_passengers = self.plane.fuel_consumption_with_passengers(passengers_count)

        self.assertEqual(13.4935, fuel_consumption_with_passengers)

    def test_max_flight_time(self):
        consumption_per_minute = 13.4935
        max_flight_time = self.plane.max_flight_time(consumption_per_minute)

        self.assertEqual(1489606, max_flight_time)

    def test_clear_fuel_consumption_per_minute(self):
        clear_fuel_consumption_per_minute = self.plane.clear_fuel_consumption_per_minute(self.plane.pk)

        self.assertEqual(13.2935, clear_fuel_consumption_per_minute)
