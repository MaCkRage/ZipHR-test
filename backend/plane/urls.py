from django.urls import path

from app.urls import router
from plane import viewsets


router.register(r'product', viewsets.PlanetViewSet, basename='plane')

urlpatterns = [
    # path(r'', views.),
]
urlpatterns += router.urls
