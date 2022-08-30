from drf_yasg import openapi

qwery_passengers_count = openapi.Parameter('passengers_count', openapi.IN_QUERY,
                                           description="Count of passengers in plane", type=openapi.TYPE_INTEGER)
