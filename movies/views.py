from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieFullSerializer, MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = MovieFullSerializer(movie)
        return Response(serializer.data)



