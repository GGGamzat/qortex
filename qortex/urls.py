from django.contrib import admin
from django.urls import path, include
from music import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/singers/', views.SingerAPIView.as_view()),
    path('api/v1/singers/<int:pk>/', views.SingerAPIView.as_view()),

    path('api/v1/songs/', views.SongAPIView.as_view()),
    path('api/v1/songs/<int:pk>/', views.SongAPIView.as_view()),

    path('api/v1/alboms/', views.AlbomAPIView.as_view()),
    path('api/v1/alboms/<int:pk>/', views.AlbomAPIView.as_view()),
]