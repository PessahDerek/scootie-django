from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

    def __str__(self):
        return self.title
