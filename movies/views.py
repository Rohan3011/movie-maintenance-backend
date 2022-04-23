from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'date_of_release']


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [OrderingFilter]
