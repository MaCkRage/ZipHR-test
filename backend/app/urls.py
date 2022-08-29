import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns_requirements = [
    # path('', views.index),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('admin/auth/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns_app = [
    path('plane/', include('plane.urls'))
]

urlpatterns_static = static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

urlpatterns_media = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns = [
    *urlpatterns_requirements,
    *urlpatterns_app,
    *urlpatterns_media,
    *urlpatterns_static,
]
