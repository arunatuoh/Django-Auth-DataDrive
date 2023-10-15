from rest_framework import serializers
from .models import Folder, File

class FolderSerializer(serializers.ModelSerializer):
    """Serializer class for the Folder model."""
    class Meta:
        model = Folder
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    """Serializer class for the File model."""
    class Meta:
        model = File
        fields = '__all__'