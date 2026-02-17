from django.shortcuts import render
from blog.models import Blog
from blog.serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .services.weather_service import fetch_weather_data

class BlogListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListWeatherData(APIView):
    def get(self, request):
        print(fetch_weather_data("London"))

    



    