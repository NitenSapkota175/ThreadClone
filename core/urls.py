from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, LikeViewSet, RepostViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"likes", LikeViewSet, basename="like")
router.register(r"reposts", RepostViewSet, basename="repost")
router.register(r"users", UserViewSet, basename="user")
urlpatterns = [
    path("", include(router.urls)),
]
