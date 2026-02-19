from rest_framework import serializers
from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Movies
        