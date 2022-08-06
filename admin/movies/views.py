from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, User
from .seralizer import MovieSeralizer
import random


class MovieViewSet(viewsets.ViewSet):
    def get(self, req):
        movies = Movie.objects.all()
        searlizer = MovieSeralizer(movies, many=True)
        return Response(searlizer.data)

    def add(self, req): 
        serializer = MovieSeralizer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def getById(self, req, pk=None):
        movie = Movie.objects.get(id=pk)
        serializer = MovieSeralizer(movie)
        return Response(serializer.data)

    def update(self, req, pk=None): 
        movie = Movie.objects.get(id=pk)
        serializer = MovieSeralizer(instance=movie, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, req, pk=None): 
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({ 'id': user.id })


    

    




