from django.contrib import admin
from django.urls import path, include

# ** Third Party Imports **
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="RESERVATION API",
        default_version='Version 1.0',
        description="All API endpoints",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shukranrma@gmail.com"),
        license=openapi.License(name="No License Yet"),
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('reservation.urls')),
    path('api/v1.0/swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # Swagger UI
]


admin.site.site_header = "Reservation Admin Panel"
admin.site.site_title = "Reservation Admin Portal"
admin.site.index_title = "Welcome to Reservation"