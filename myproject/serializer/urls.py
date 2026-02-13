from django.urls import path
from .views import BookListView

urlpatterns = [
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookListView.as_view())
]
