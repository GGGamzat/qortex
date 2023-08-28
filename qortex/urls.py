from django.contrib import admin
from django.urls import path, include
from music import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('api_schema', get_schema_view(title='API Schema', description='info qortex'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/singers/', views.SingerAPIView.as_view()),
    path('api/v1/singers/<int:pk>/', views.SingerAPIView.as_view()),

    path('api/v1/songs/', views.SongAPIView.as_view()),
    path('api/v1/songs/<int:pk>/', views.SongAPIView.as_view()),

    path('api/v1/alboms/', views.AlbomAPIView.as_view()),
    path('api/v1/alboms/<int:pk>/', views.AlbomAPIView.as_view()),
]