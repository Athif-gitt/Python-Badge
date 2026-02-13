from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status



class BookListView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:

            book = Book.objects.get(pk=pk)

        except Book.DoesNotExist:
            return Response({"message": "The book doesnt exist"})
        serializer = BookSerializer(book)

        book.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

