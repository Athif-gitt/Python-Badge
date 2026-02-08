from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import BookSerializer
from .models import Book
from rest_framework import serializers


class BookSerializerView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddBookSerializerView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Succesful"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateBookeSerializerPrice(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(
                {"message": "book not present"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = BookSerializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Book updated successfully"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

