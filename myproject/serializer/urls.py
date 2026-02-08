from django.urls import path
from .views import BookSerializerView, AddBookSerializerView, UpdateBookeSerializerPrice

urlpatterns = [
    path('', BookSerializerView.as_view()),
    path('add/', AddBookSerializerView.as_view()),
    path('<int:pk>/', UpdateBookeSerializerPrice.as_view()),
]
