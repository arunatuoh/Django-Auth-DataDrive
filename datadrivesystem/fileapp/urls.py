from django.urls import path
from .views import FolderListCreateView, FolderRetrieveUpdateDestroyView, FileListCreateView, FileRetrieveUpdateDestroyView

urlpatterns = [
    # Folder URLs
    path('folders/', FolderListCreateView.as_view(), name='folder-list-create'),
    path('folders/<int:pk>/', FolderRetrieveUpdateDestroyView.as_view(), name='folder-retrieve-update-destroy'),

    # File URLs
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileRetrieveUpdateDestroyView.as_view(), name='file-retrieve-update-destroy'),
]
