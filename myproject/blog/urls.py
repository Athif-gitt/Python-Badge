from django.urls import path
from .views import BlogEditView


urlpatterns = [
    # path('<int:id>/', post_detail, name='post_detail'),
    path('blog/', BlogEditView.as_view()),
    path('blog/<int:pk>/', BlogEditView.as_view()),
]
