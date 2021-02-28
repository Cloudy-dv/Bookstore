from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lib.views import BooksListView, Manage, Add, Update, Delete, import_books, Found, BooksListApiView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('book list')
        self.assertEquals(resolve(url).func.__name__, BooksListView.as_view().__name__)

    def test_manage_url_is_resolved(self):
        url = reverse('manage')
        self.assertEquals(resolve(url).func.__name__, Manage.as_view().__name__)

    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.__name__, Add.as_view().__name__)

    def test_import_url_is_resolved(self):
        url = reverse('import')
        self.assertEquals(resolve(url).func.__name__, import_books.__name__)

    def test_found_url_is_resolved(self):
        url = reverse('found')
        self.assertEquals(resolve(url).func.__name__, Found.as_view().__name__)

    def test_api_url_is_resolved(self):
        url = reverse('api')
        self.assertEquals(resolve(url).func.__name__, BooksListApiView.as_view().__name__)
