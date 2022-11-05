from musicapp.models import Song, Artiste, Lyric
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('artiste_id', 'title', 'date_released', 'likes')


class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artiste
        fields = ('first_name', 'last_name', 'age')


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ('content', 'song_id')
