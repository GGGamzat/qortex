from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from rest_framework import generics

from .models import Singer, Song, Albom
from .serializers import SingerSerializer, SongSerializer, AlbomSerializer


class SingerAPIList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SingerAPIUpdate(generics.UpdateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongAPIList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongAPIUpdate(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class AlbomAPIList(generics.ListCreateAPIView):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

class AlbomAPIUpdate(generics.UpdateAPIView):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer


# class SingerAPIView(APIView):
#     def get(self, request):
#         singers = Singer.objects.all()
#         return Response({'singers': SingerSerializer(singers, many=True).data})
#
#     def post(self, request):
#         serializer = SingerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         singer_new = Singer.objects.create(
#             name=request.data['name']
#         )
#         return Response({'post': SingerSerializer(singer_new).data})
#
#
# class SongAPIView(APIView):
#     def get(self, request):
#         songs = Song.objects.all()
#         return Response({'songs': SongSerializer(songs, many=True).data})
#
#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         song_new = Song.objects.create(
#             name=request.data['name'],
#             singer=request.data['singer']
#         )
#         return Response({'post': SongSerializer(song_new).data})
#
#
# class AlbomAPIView(APIView):
#     def get(self, request):
#         alboms = Albom.objects.all()
#         return Response({'alboms': AlbomSerializer(alboms, many=True).data})
#
#     def post(self, request):
#         serializer = AlbomSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         albom_new = Albom.objects.create(
#             name=request.data['name'],
#             singer=request.data['singer'],
#             song=request.data['song'],
#             date=request.data['date']
#         )
#         return Response({'post': AlbomSerializer(albom_new).data})