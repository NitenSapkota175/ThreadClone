from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, LikeViewSet, RepostViewSet
from users.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"likes", LikeViewSet, basename="like")
router.register(r"reposts", RepostViewSet, basename="repost")
router.register(r"users", UserViewSet, basename="user")
urlpatterns = [
    path("", include(router.urls)),
    path("jwt/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
