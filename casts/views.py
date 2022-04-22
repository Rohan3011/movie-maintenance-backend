from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from actors.models import Actor
from actors.serializers import ActorSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer

from .models import Cast
from .serializers import CastSerializer


class CastView(APIView):
    """Provides cast details of a every movie"""
    model = Cast
    serializer_class = CastSerializer

    def get(self, request, format=None):
        queryset = self.model.objects.all()
        casts = self.serializer_class(queryset, many=True).data
        return Response(casts, status=status.HTTP_200_OK)


class ActorCastView(APIView):
    """ Provides cast(s) details of a movie"""

    model = Cast
    serializers_class = MovieSerializer

    def post(self, request, format=None):
        actor = request.data.get('actor')
        data = self.model.objects.filter(actor=actor)
        movies = []
        for cast in data:
            movies.append(Movie.objects.get(id=cast.movie.id))
        movies = self.serializers_class(
            movies, many=True, context={"request": request})
        return Response(movies.data, status=status.HTTP_200_OK)


class MovieCastView(APIView):
    """ Provides movie(s) done by actor"""

    model = Cast
    serializers_class = ActorSerializer

    def post(self, request, format=None):
        movie = request.data.get('movie')
        data = self.model.objects.filter(movie=movie)
        actors = []
        for cast in data:
            actors.append(Actor.objects.get(id=cast.actor.id))
        actors = self.serializers_class(
            actors, many=True, context={"request": request})
        return Response(actors.data, status=status.HTTP_200_OK)
