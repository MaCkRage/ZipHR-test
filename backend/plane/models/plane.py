import math

from django.db import models
from django.conf import settings


class Plane(models.Model):
    tank_capacity = models.IntegerField(default=200, verbose_name='Base fuel tank capacity (liters)')

    class Meta:
        # Excuse me, I'm tired, I wrote scripts, docker-compose files and so much more, also I had so much tasks
        # at work in this period
        #  Also I didn't do admin panel, but I can :)
        pass

    @property
    def fuel_tank_capacity(self) -> int:
        """
        Get fuel tank capacity of airplane
        :return: the number of liters of fuel that the airplane's fuel tank can hold
        """

        return self.tank_capacity * self.pk

    def fuel_consumption_with_passengers(self,  passengers_count: int) -> float:
        """
        Calculate fuel consumption with passengers onboard
        :param passengers_count: count of passengers onboard
        :return: fuel consumption per minute with passengers onboard
        """

        return round(Plane.clear_fuel_consumption_per_minute(self.pk) +
                     settings.FUEL_INCREASE_PER_PASSENGER * passengers_count, 4)

    def max_flight_time(self, consumption_per_minute: float) -> int:
        """
        Calculate maximum flight time
        :param consumption_per_minute: fuel consumption when there are no passengers on board
        :return: How much time (in minutes) the aircraft will be able to hold in the air with passengers on board
        """

        return round(self.fuel_tank_capacity / consumption_per_minute)

    @staticmethod
    def clear_fuel_consumption_per_minute(airplane_id: int) -> int:
        """
        Count plane consumption per minute
        :param airplane_id: ID of airplane whose flight time we want to calculate
        :return: fuel consumption when there are no passengers on board
        """
        # HACK: logarithm of 1 to any base is 0, but fuel consumption can't be lower than 0.1 liter per minute
        #  https://www.livemint.com/news/india/flights-how-much-fuel-your-plane-consumes-per-second-11592883647441.html
        #  (in real life fuel consumption is more than 1 liter per minute)
        base_consumption = math.log2(airplane_id) or 0.1

        return round(base_consumption * settings.BASE_FUEL_CONSUMPTION_RATE, 4)
