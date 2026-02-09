from django.urls import path
from .views import ProfileUploadView

urlpatterns = [
    path("upload-profile/", ProfileUploadView.as_view(), name="upload-profile"),
]
