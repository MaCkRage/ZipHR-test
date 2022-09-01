from app.urls import router
from plane import viewsets


router.register(r'plane', viewsets.PlanetViewSet, basename='plane')

urlpatterns = [
    # path(r'', views.),
]
urlpatterns += router.urls
