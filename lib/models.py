from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=255, unique=True, null=True)
    pages = models.IntegerField(default=0)
    art_cover = models.URLField(max_length=255)
    published_lang = models.CharField(max_length=255)

    def __str__(self):
        return self.title
