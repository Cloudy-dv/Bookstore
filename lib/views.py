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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Add(CreateView):
    model = Books
    template_name = "addbook.html"
    form_class = BookForm
    success_url = '/manage'

    def form_valid(self, form):
        return super().form_valid(form)


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
            s = search_request(cd)
            for data in s['items']:
                volume_info = data['volumeInfo']

                if len(volume_info['publishedDate']) == 4:
                    date = datetime.date(int(volume_info['publishedDate']), 1, 1)
                elif len(volume_info['publishedDate']) > 4:
                    year, month, day = volume_info['publishedDate'].split('-')
                    date = datetime.date(int(year), int(month), int(day))
                else:
                    date = None
                book_found = Books.objects.get(isbn=volume_info.get('industryIdentifiers')[0]['identifier'])
                if not book_found:
                    book = Books(
                        title=volume_info.get('title'),
                        author=str(volume_info.get('authors')),
                        publication_date=date,
                        isbn=volume_info.get('industryIdentifiers')[0]['identifier'],
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def search_request(cd):
    search_str = "https://www.googleapis.com/books/v1/volumes?q="
    key = "&key=AIzaSyCCZjyPr-mG7okp8AQyX0YbbZmjBuNuPUA"
    cd = {x: y for x, y in cd.items() if y}
    text = ""
    except_key = list(cd.keys())[0]
    for x, y in cd.items():
        if except_key == x:
            text += f'{y}'
        else:
            text += f'+{x}:{y}'
    url = search_str + text + key
    req = requests.get(url)
    return req.json()


class BooksListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
