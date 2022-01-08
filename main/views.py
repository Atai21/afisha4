from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import MovieListSerializer, GenreListSerializer
from .models import Movie, Genre
from rest_framework import status
@api_view(['GET'])
def get_data(request):
    context = {
        'number': 1,
        'text': 'ogo go',
        'bool': True,
        'list': [1, 2, 3]
    }
    return Response(data=context)

@api_view(["GET", 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieListSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        title = request.data['title']
        description = request.data['description']
        genre_id = request.data['genre_id']
        movies = Movie.objects.create(
            title=title,
            description=description,
            genre_id=genre_id
        )
        return Response(data={'message': 'OK'})

@api_view(['GET'])
def movie_detail_view(request, id):
            try:
                movie = Movie.objects.get(id=id)
            except Movie.DoesNotExist:
                return Response(data={'message': 'Product not found'},
                                status=status.HTTP_404_NOT_FOUND)
            data = MovieListSerializer(movie).data
            return Response(data=data)

@api_view(['GET'])
def genres_view(request):
    genres = Genre.objects.all()

    data = GenreListSerializer(genres, many=True).data

    return Response(data=data)