from rest_framework import serializers
from .models import Books

class DumpSerializer(serializers.ModelSerializer):

    price = serializers.IntegerField( read_only=True)

    class Meta:
        model = Books
        fields = '__all__'



