from rest_framework import serializers
from main.models import Movie, Review
from rest_framework import serializers
from main.models import Movie, Genre

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']

class MovieListSerializer(serializers.ModelSerializer):
    cinema = serializers.SerializerMethodField(source='get_cinema')
    genres = serializers.SerializerMethodField(source='get_genres')
    reviews = serializers.SerializerMethodField(source='get_reviews')
    class Meta:
        model = Movie
        #fields = '__all__'
        fields = ['id', 'title', 'description', 'cinema', 'genres', 'reviews']
    def get_cinema(self, obj):
        return obj.cinema.name

    def get_genres(self, obj):
        return GenreListSerializer(obj.genres, many=True).data

    def get_reviews(self, obj):
        return ReviewListSerializer(obj.reviews, many=True).data
