from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer

class ProfileUploadView(APIView):

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

