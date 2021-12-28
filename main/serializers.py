from rest_framework import serializers
from main.models import Movie
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #fields = '__all__'
        fields = ['id', 'title', 'description', 'cinema',] #'genres']