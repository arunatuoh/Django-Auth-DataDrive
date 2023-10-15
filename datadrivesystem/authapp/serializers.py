from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the CustomUser model.
    Serializes user data, including email, password, first name, and last name
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')
