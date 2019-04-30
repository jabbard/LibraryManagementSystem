from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from searchableselect.widgets import SearchableSelect

class BookForm(forms.ModelForm):
    book_id = forms.CharField(label='Book ID')
    book_name = forms.CharField(label='Book Name')
    ISBN = forms.CharField(label='ISBN')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = self.fields['author'].queryset.order_by('author_name')

    class Meta:
        model = Books
        #fields = ['book_id', 'book_name', 'ISBN', 'description', 'author', 'publisher', 'edition', 'type', 'genre']
        exclude = ()
        widgets = {
            'author':SearchableSelect(model='Authors', search_field='author_name', many=True)
        }




class GenreForm(forms.ModelForm):
    genre_id = forms.CharField(label='Genre ID')
    genre_name = forms.CharField(label='Genre Name')
    description = forms.Textarea()
    class Meta:
        model = Genres
        fields = ['genre_id', 'genre_name', 'description']

class AuthorForm(forms.ModelForm):
    author_id = forms.CharField(label='Author ID')
    author_name = forms.CharField(label="Author's Name")
    class Meta:
        model = Authors
        fields = ['author_id', 'author_name']

class PublisherForm(forms.ModelForm):
    publish_id = forms.CharField(label='Publisher ID')
    publisher_name = forms.CharField(label='Publisher Name')
    class Meta:
        model = Publishers
        fields = ['publish_id', 'publisher_name', 'city']

class FacultyForm(forms.ModelForm):
    f_id = forms.CharField(label='Faculty ID')
    f_name = forms.CharField(label='Faculty Name')

    class Meta:
        model = Faculty
        fields = ['f_id', 'f_name']

class StudentForm(forms.ModelForm):
    s_id = forms.CharField(label='Student ID')
    st_name = forms.CharField(label='Student Name')
    ph_num = forms.CharField(label='Phone Number')
    email = forms.EmailField(label='Email')


    class Meta:
        model = Students
        fields = ['s_id', 'st_name', 'ph_num', 'email', 'faculty']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class IssueForm(forms.Form):
    b_id = forms.ModelChoiceField(label="Barcode", queryset=Book_Number.objects.all())
    student_id = forms.CharField(label="Student ID")

class ReturnForm(forms.Form):
    book_id = forms.ModelChoiceField(label="Book ID", queryset=Book_Number.objects.filter(status='Taken'))


class StructuresForm(forms.ModelForm):
    class Meta:
        model = Structures
        fields = ['fine', 'days']