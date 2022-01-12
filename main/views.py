from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import MovieListSerializer, GenreListSerializer, MovieValidateSerializer, \
    MovieDetailValidateSerializer
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
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data['title']
        description = request.data['description']
        cinema_id = request.data['cinema_id']
        movie = Movie.objects.create(
            title=title,
            description=description,
            cinema_id=cinema_id
        )
        movie.genres.set(request.data['genres'])
        movie.save()
        return Response(data={'message': 'OK'})

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Product not found'},
                                status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieListSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Movie Deleted'})
    else:
        serializer = MovieDetailValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data['title']
        description = request.data['description']
        cinema_id = request.data['cinema_id']
        genres = request.data['genres']
        movie.title = title
        movie.description = description
        movie.cinema_id = cinema_id
        movie.genres.set(genres)
        movie.save()
        return Response(data=MovieListSerializer(movie).data)

@api_view(['GET'])
def genres_view(request):
    genres = Genre.objects.all()

    data = GenreListSerializer(genres, many=True).data

    return Response(data=data)