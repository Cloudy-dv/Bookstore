from django.test import TestCase, Client
from django.urls import reverse
from lib.models import Books



class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.list_url = reverse('book list')
        self.manage = reverse('manage')
        self.add = reverse('add')
        self.importbooks = reverse('import')
        self.found = reverse('found')


    def test_project_books_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'showbooks.html')

    def test_project_manage_GET(self):
        response = self.client.get(self.manage)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage.html')

    def test_project_add_GET(self):
        response = self.client.post(self.add, {
            'title': 'testcase',
            'author': 'testcaseaut',
            'publication_date': '2222-01-01',
            'isbn': '100',
            'pages': 100,
            'art_cover': "https://github.com/Cloudy-dv/Bookstore",
            'published_lang': 'TESTLANG',

        })
        self.assertEquals(response.status_code, 302)

    def test_project_importbooks_GET(self):
        response = self.client.get(self.importbooks)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'import.html')

    def test_project_found_GET(self):
        response = self.client.get(self.found)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'found.html')

