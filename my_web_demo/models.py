from django.db import models
from django.db.models.fields import files

# Create your models here.

# models.py (define your data structure)
# models.py (define your data structure)
# model create for table

class ProductImage(models.Model):
    
    image = models.ImageField(upload_to='images/')
    files = "__all__"
    def __str__(self):
        return self.image
    