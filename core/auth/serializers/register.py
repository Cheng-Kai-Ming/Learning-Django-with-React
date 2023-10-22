from rest_framework import serializers

from core.user.models import User
from core.user.serializers import UserSerializer

class RegisterSerializer(UserSerializer):
    """
    Register Serializer for requests and  user creation
    """
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'username', 'email', 'password', 'first_name', 'last_name']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
