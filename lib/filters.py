import django_filters
from .models import Books


class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Books
        fields = {
            'title': ['contains'],
            'author': ['contains'],
            'published_lang': ['contains'],
            'publication_date': ['gt', 'lt']
        }
