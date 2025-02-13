from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.school.urls import school_urlpatterns

schema_view = get_schema_view(
    info = openapi.Info(
        title="School API Documentation",
        default_version='v1',
        description="School App API Documentation with Swagger / OpenAPI 2.0",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public = True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(school_urlpatterns)),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]