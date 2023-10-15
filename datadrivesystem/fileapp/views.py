from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Folder, File
from .serializers import FolderSerializer, FileSerializer

# Create, List folders
class FolderListCreateView(generics.ListCreateAPIView):
    """
    Allows users to create new folders and retrieve a list of all folders.
    Successful folder creation returns folder details and a success message.
    Successful folder retrieval returns a list of folders and a success message.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def post(self, request, *args, **kwargs):
        # Create a new folder
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Folder created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # Retrieve all folders
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'message': 'Folders retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

# Retrieve, Update, Delete a folder
class FolderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows users to retrieve, update, and delete a specific folder.
    Successful folder retrieval returns folder details and a success message.
    Successful folder update returns updated folder details and a success message.
    Successful folder deletion returns a success message
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def update(self, request, *args, **kwargs):
        # Update a folder
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Folder updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Delete a folder
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Folder deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        # Retrieve a folder
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'message': 'Folder retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

# Create, List files
class FileListCreateView(generics.ListCreateAPIView):
    """
    Allows users to create new files and retrieve a list of all files.
    Successful file creation returns file details and a success message.
    Successful file retrieval returns a list of files and a success message.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        # Create a new file
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'File created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # Retrieve all files
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'message': 'Files retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

# Retrieve, Update, Delete a file
class FileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows users to retrieve, update, and delete a specific file.
    Successful file retrieval returns file details and a success message.
    Successful file update returns updated file details and a success message.
    Successful file deletion returns a success message.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def update(self, request, *args, **kwargs):
        # Update a file
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'File updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Delete a file
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        # Retrieve a file
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'message': 'File retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
