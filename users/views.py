from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):

        if self.action == "create":  # Allow anyone to register
            permission_classes = [permissions.AllowAny]
        else:  # Restrict other actions to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
