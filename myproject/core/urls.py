from django.urls import path
from .views import MoviesView

urlpatterns = [
    
    path('<int:pk>/', MoviesView.as_view()),
]
