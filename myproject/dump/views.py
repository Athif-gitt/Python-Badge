from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import DumpSerializer
from .models import Books
from rest_framework import viewsets

class DumpView(APIView):

    def get(self, request):

        books = Books.objects.all()


        serializer = DumpSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):

        try:
            book = Books.objects.get(pk=pk)

            serializer = DumpSerializer(book, data=request.data, partial=True)

        except Books.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        try:
            book = Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response({"message": "Deleted!"}, status=status.HTTP_410_GONE)
    
class DumpGenericView(viewsets.ModelViewSet):

    queryset = Books.objects.all()
    serializer_class = DumpSerializer













