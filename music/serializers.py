from .models import Singer, Song, Albom
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('id', 'name')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'singer')


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('id', 'name', 'singer', 'song', 'date')