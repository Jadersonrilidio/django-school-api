from django.contrib import admin
from django.urls import path, include
from apps.school.urls import school_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(school_urlpatterns)),
]
