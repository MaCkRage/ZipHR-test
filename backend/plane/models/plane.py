import math

from django.db import models
from django.conf import settings


class Plane(models.Model):
    tank_capacity = models.IntegerField(default=200, verbose_name='Base fuel tank capacity (liters)')

    class Meta:
        pass

    @property
    def fuel_tank_capacity(self) -> int:
        """
        Get fuel tank capacity of airplane
        :return: the number of liters of fuel that the airplane's fuel tank can hold
        """
        return self.tank_capacity * self.pk

    @classmethod
    def base_fuel_consumption(cls, airplane_fuel_consumption) -> int:
        """

        """
        # HACK: logarithm of 1 to any base is 0, but fuel consumption can't be lower than 1.0 liter per minute
        #  https://www.livemint.com/news/india/flights-how-much-fuel-your-plane-consumes-per-second-11592883647441.html
        #  (in real life fuel consumption is more than 1 liter per minute)
        consumption = round(math.log2(airplane_fuel_consumption), 3) or 0.1

        return consumption * settings.BASE_FUEL_CONSUMPTION_RATE

    @classmethod
    def fuel_consumption(cls):
        pass
