from django.urls import path
from .views import DumpView

urlpatterns = [
    path('', DumpView.as_view()),
    path('<int:pk>/', DumpView.as_view()),
]
