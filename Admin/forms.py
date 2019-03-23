from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_id', 'book_name', 'ISBN', 'description', 'publisher', 'edition', 'type', 'genre']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ['genre_id', 'genre_name', 'description']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['author_id', 'author_name']

class PublisherForm(forms.ModelForm):
    publish_id = forms.CharField(label='Publisher ID')
    class Meta:
        model = Publishers
        fields = ['publish_id', 'publisher_name', 'city']