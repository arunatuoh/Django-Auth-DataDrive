from django.db import models

# Create your models here.

class Folder(models.Model):
    """Model class for the Folder"""
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

class File(models.Model):
    """Model class for the File"""
    file = models.FileField(upload_to='uploads/')
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True, blank=True)
