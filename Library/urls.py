from django.contrib import admin
from django.urls import path
from lib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", views.BooksListView.as_view(), name="book list"),
    path("manage/", views.Manage.as_view(), name="manage"),
    path("manage/addbook/", views.Add.as_view(), name='add'),
    path("manage/<int:id>/update/", views.Update.as_view(), name='update'),
    path("manage/<int:id>/delete/", views.Delete.as_view(), name='delete'),
    path("import/", views.import_books, name="import"),
    path("import/found", views.Found.as_view(), name="found"),
    path('api/view', views.BooksListApiView.as_view(), name='api'),
]