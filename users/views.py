from rest_framework import viewsets, mixins, permissions
from .models import CustomUser
from .serializers import UserRegistrationSerializer

class UserRegistrationViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]