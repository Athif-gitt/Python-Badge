from django.urls import path
from .views import BlogEditView, BlogListView, DjangoBlogView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('<int:id>/', post_detail, name='post_detail'),
    path('blog/', BlogEditView.as_view()),
    path('blog/<int:pk>/', BlogEditView.as_view()),
    path('dblog/', DjangoBlogView.as_view()),
]

router = DefaultRouter()
router.register(r'blogs', BlogListView)

urlpatterns += router.urls


