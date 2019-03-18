from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
def home(request):

    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

def books(request):
    book_list = Books.objects.all()
    return render(request, "tables.html", {'book_list': book_list})

def add_books(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book')

    return render(request, "new_book.html", {'form':form})

def update_book(request, id):
    book = Books.objects.get(book_id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book')
    return render(request, "new_book.html", {'form':form, 'book':book})

def delete_book(request, id):
    book = Books.objects.get(book_id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book')

    return render(request, "confirmation.html", {'book':book})