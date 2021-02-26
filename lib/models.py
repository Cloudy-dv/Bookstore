from django.db import models
from django.urls import reverse

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField(default=0)
    art_cover = models.URLField(max_length=100)
    published_lang = models.CharField(max_length=20)

    def __str__(self):
        return self.title
