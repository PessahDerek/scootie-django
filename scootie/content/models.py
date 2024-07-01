from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name + f" ({self.rating})"
