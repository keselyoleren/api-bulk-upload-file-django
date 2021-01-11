from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/")

class BulkFile(models.Model):
    file = models.FileField(upload_to="tmp/")