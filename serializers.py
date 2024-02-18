# myapp/serializers.py

from rest_framework import serializers
from .models import UserProfile, ShoppingHistory

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ShoppingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingHistory
        fields = '__all__'
