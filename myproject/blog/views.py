from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer



class BlogEditView(APIView):

    def get_blog(self, pk):
        try:
            Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None
    
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        # blog = self.get_blog(pk)
        # if not blog:
        #     return Response({"error": "not found"})

        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"message": "Blog not founded"})
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,  pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"message": "Blog not founded"})
        # serializer = BlogSerializer(blog)
        blog.delete()
        return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"message": "Blog not founded"})
        
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        
    



    



            


        


