from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=100, unique=True)
    pages = models.IntegerField(default=0)
    art_cover = models.URLField(max_length=100)
    published_lang = models.CharField(max_length=20)

    def __str__(self):
        return self.title
