from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .filters import BookFilter
from .forms import BookForm
from .models import Books

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def book_add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'addbook.html', context)


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