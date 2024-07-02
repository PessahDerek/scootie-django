import time

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


class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['id']


class Contact(models.Model):
    choices = (
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'Whatsapp'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
    )
    type = models.CharField(max_length=100, choices=choices, default='phone')
    contact = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.link:
            if self.type == 'phone':
                self.link = f"tel:{self.contact}"
            if self.type == 'email':
                self.link = f"mailto:{self.contact}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type}: {self.contact}"

    class Meta:
        ordering = ['contact']
