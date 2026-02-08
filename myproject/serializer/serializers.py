from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(min_value=1)
    class Meta:
        model = Book
        fields = '__all__'

        def validate_price(self, value):
            if value <= 0 :
                raise serializers.ValidationError("Price must be positive ang gt 0")
            return value
        
        def validate(self, data):
            if data.get("author") == "Admin" and data.get("price", 0) < 1000:
                raise serializers.ValidationError(
            "Admin books must cost at least 1000"
        )
            return data
        
class FirstSerializer(serializers.ModelSerializer):
    model = Book
    fields = '__all__'

class Second(serializers.ModelSerializer):
    book = FirstSerializer()


    model = Book
    fields = ['']

        

        
    
