from .models import Movies
from .serializer import MoviesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MoviesView(APIView):

    def get(self, request, pk):

        try:

            movie = Movies.objects.get(pk=pk)

            serializer = MoviesSerializer(movie)
        except Movies.DoesNotExist:
            return Response({"message": "Object not fpund"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):

        try:

            movie = Movies.objects.get(pk=pk)

            serializer = MoviesSerializer(movie, data=request.data, partial=True)

        except Movies.DoesNotExist:

            return Response({"message": "Object not fpund"}, status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


        




        