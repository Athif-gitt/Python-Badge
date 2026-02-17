from django.urls import path
from .views import BlogListView, ListWeatherData

urlpatterns = [
    path('blog/', BlogListView.as_view()),
    path('weather/', ListWeatherData.as_view()),
]
