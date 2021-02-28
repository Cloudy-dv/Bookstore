from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import BookFilter
from .forms import BookForm, BookImport
from .models import Books
from .serializers import BookSerializer
from rest_framework import generics
import requests
import datetime


class BooksListView(ListView):
    model = Books
    template_name = 'showbooks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Manage(ListView):
    model = Books
    template_name = "manage.html"
    context_object_name = 'books'


class Add(CreateView):
    model = Books
    template_name = "addbook.html"
    form_class = BookForm
    success_url = '/manage'


class Update(UpdateView):
    model = Books
    template_name = "update.html"
    form_class = BookForm
    success_url = '/manage'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Books, id=id_)


class Delete(DeleteView):
    model = Books
    template_name = "delete.html"
    form_class = BookForm
    success_url = '/manage'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Books, id=id_)


def import_books(request):
    if request.method == 'POST':
        form = BookImport(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            search = search_request(cd)
            for data in search.get('items', []):
                volume_info = data['volumeInfo']

                if volume_info.get('publishedDate', None) is None:
                    date = None
                elif len(volume_info['publishedDate']) == 4:
                    date = datetime.date(int(volume_info['publishedDate']), 1, 1)
                elif len(volume_info['publishedDate']) == 7:
                    year, month = volume_info['publishedDate'].split('-')
                    date = datetime.date(int(year), int(month), 1)
                elif len(volume_info['publishedDate']) > 7:
                    year, month, day = volume_info['publishedDate'].split('-')
                    date = datetime.date(int(year), int(month), int(day))
                else:
                    date = None

                if volume_info.get('industryIdentifiers'):
                    book_found = Books.objects.filter(isbn=volume_info.get('industryIdentifiers')[0]['identifier'])
                    isbn = volume_info.get('industryIdentifiers')[0]['identifier']
                else:
                    book_found = None
                    isbn = None

                if not book_found:
                    book = Books(
                        title=volume_info.get('title'),
                        author=str(volume_info.get('authors')),
                        publication_date=date,
                        isbn=isbn,
                        pages=volume_info.get('pageCount') or 0,
                        art_cover=volume_info.get('previewLink'),
                        published_lang=volume_info.get('language')
                    )
                    book.save()
            return redirect("/import/found")
    else:
        form = BookImport()
    return render(request, 'import.html', {'form': form})


class Found(ListView):
    model = Books
    template_name = "found.html"
    context_object_name = 'books'


def search_request(cd):
    search_str = "https://www.googleapis.com/books/v1/volumes?q="
    key = "&key=AIzaSyCCZjyPr-mG7okp8AQyX0YbbZmjBuNuPUA"
    cd = {x: y for x, y in cd.items() if y}
    text = ""
    for x, y in cd.items():
        text += f'{x}:{y}+'
    url = search_str + text + key
    req = requests.get(url)
    return req.json()


class BooksListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
