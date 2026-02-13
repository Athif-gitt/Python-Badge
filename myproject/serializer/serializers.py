from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Book

        