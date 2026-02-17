from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(min_length=8)
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True, "min_length": 8} #field level validation
        }
        

    
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords dont match")
        return data
    
    def create(self, validated_data):

        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)
    

    
