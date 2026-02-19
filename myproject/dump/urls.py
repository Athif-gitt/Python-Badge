from django.urls import path, include
from .views import DumpView, DumpGenericView
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', DumpView.as_view()),
#     path('<int:pk>/', DumpView.as_view()),
# ]

router = DefaultRouter()
router.register(r'books', DumpGenericView)
urlpatterns = [
    path('', include(router.urls)),
]


