import django_filters
from .models import Books
from django.db import models
from django import forms


class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Books
        fields = {
            'title': ['contains'],
            'author': ['contains'],
            'published_lang': ['contains'],
            'publication_date': ['gt', 'lt']
        }
