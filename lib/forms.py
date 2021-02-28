from django import forms
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class BookImport(forms.Form):
    intitle = forms.CharField(max_length=100, required=False, empty_value=None)
    inauthor = forms.CharField(max_length=100, required=False, empty_value=None)
    inpublisher = forms.CharField(max_length=100, required=False, empty_value=None)
    isbn = forms.CharField(max_length=13, required=False, empty_value=None)
    lccn = forms.CharField(max_length=30, required=False, empty_value=None)
    oclc = forms.CharField(max_length=20, required=False, empty_value=None)
