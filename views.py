# myapp/views.py

from rest_framework import viewsets
from .models import UserProfile, ShoppingHistory
from .serializers import UserProfileSerializer, ShoppingHistorySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ShoppingHistoryViewSet(viewsets.ModelViewSet):
    queryset = ShoppingHistory.objects.all()
    serializer_class = ShoppingHistorySerializer
