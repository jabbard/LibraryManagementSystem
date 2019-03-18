from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_id', 'book_name', 'description', 'type', 'genre']