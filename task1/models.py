from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class MyFiles(models.Model):
    id = models.AutoField( primary_key=True)
    file_name = models.CharField(max_length=200)
    file_data = models.FileField(upload_to='maps', storage=gd_storage)