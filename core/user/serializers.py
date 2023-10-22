from rest_framework import serializers
from core.user.models import User
from core.abstract.serializers import AbstractSerializer

class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'public_id', 'bio', 'avatar', 'created', 'updated', 'email', 'is_active']
        read_only_fields = ['is_active']
