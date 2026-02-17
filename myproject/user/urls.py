from django.urls import path
from .views import UserSerializerView, UserLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urlpatterns = [
#     
# ]

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # path('register/', UserSerializerView.as_view()),
    # path('login/', UserLoginView.as_view()),
]
