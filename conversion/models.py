from django.db import models

# Create your models here.
class Files(models.Model):
    file = models.FileField(upload_to="docs/",max_length=899,null=True,default=None)
