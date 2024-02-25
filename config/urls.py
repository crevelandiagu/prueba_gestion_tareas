from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

from app_task_manager.views import Health

schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager",
        default_version='v1',
        description="Documentacion api",
        contact=openapi.Contact(email="crevelandiagu@unal.edu.co"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('ping/', Health.as_view(), name='health'),
    path('admin/', admin.site.urls),
    path(r'api/', include('app_task_manager.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
  ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
