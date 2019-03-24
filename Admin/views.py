from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm, GenreForm, AuthorForm, PublisherForm, FacultyForm, StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def books(request):
    book_list = Books.objects.all()
    return render(request, "tables.html", {'book_list': book_list})

@login_required
def add_books(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book')

    return render(request, "new_book.html", {'form':form})

@login_required
def update_book(request, id):
    book = Books.objects.get(book_id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book')
    return render(request, "new_book.html", {'form':form, 'book':book})

@login_required
def delete_book(request, id):
    book = Books.objects.get(book_id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book')

    return render(request, "confirmation.html", {'book': book})

@login_required
def genres(request):
    genre_list = Genres.objects.all()
    return render(request, "genres.html", {'genre_list': genre_list})

@login_required
def add_genre(request):
    form = GenreForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('genre')

    return render(request, "new_genre.html", {'form': form})

@login_required
def update_genre(request, id):
    genre = Genres.objects.get(genre_id=id)
    form = GenreForm(request.POST or None, instance=genre)

    if form.is_valid():
        form.save()
        return redirect('genre')

    return render(request, "new_genre.html", {'form': form, 'genre': genre})

@login_required
def delete_genre(request, id):
    genre = Genres.objects.get(genre_id=id)

    if request.method == 'POST':
        genre.delete()
        return redirect('genre')

    return render(request, "confirmation.html", {'genre': genre})

@login_required
def authors(request):
    author = Authors.objects.all()

    return render(request,"authors.html", {'author':author})

@login_required
def add_author(request):
    form = AuthorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('author')

    return render(request, "new_author.html", {'form':form})

@login_required
def update_author(request, id):
    author = Authors.objects.get(author_id=id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('author')

    return render(request,"new_author.html", {'form':form, 'author':author})

@login_required
def delete_author(request, id):
    authors = Authors.objects.get(author_id=id)

    if request.method == 'POST':
        authors.delete()
        return redirect('author')

    return render(request, "confirmation.html", {'author': authors})

@login_required
def publisher(request):
    publishers = Publishers.objects.all()

    return render(request, "publishers.html", {'publishers':publishers})

@login_required
def add_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('publisher')

    return render(request, "new_publisher.html", {'form':form})

@login_required
def update_publisher(request, id):
    publisher = Publishers.objects.get(publish_id=id)
    form = PublisherForm(request.POST or None, instance=publisher)

    if form.is_valid():
        form.save()
        return redirect('publisher')

    return render(request, "new_publisher.html", {'form':form, 'publishers':publisher})

@login_required
def delete_publisher(request, id):
    publisher = Publishers.objects.get(publish_id = id)
    if request.method == "POST":
        publisher.delete()
        return redirect('publisher')

    return render(request, "confirmation.html", {'publisher':publisher})

@login_required
def faculty(request):
    faculties = Faculty.objects.all()

    return render(request, "faculties.html", {'faculty':faculties})

@login_required
def add_faculty(request):
    form = FacultyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('faculty')

    return render(request, "new_faculty.html", {'form': form})

@login_required
def update_faculty(request, id):
    faculty = Faculty.objects.get(f_id=id)

    form = FacultyForm(request.POST or None, instance=faculty)

    if form.is_valid():
        form.save()
        return redirect('faculty')

    return render(request, "new_faculty.html", {'form': form, 'faculties': faculty})

@login_required
def delete_faculty(request,id):
    faculty = Faculty.objects.get(f_id=id)

    if request.method == "POST":
        faculty.delete()
        return redirect('faculty')

    return render(request, "confirmation.html", {'faculties': faculty})

@login_required
def student(request):
    student = Students.objects.all()

    return render(request,"students.html", {'students':student})

@login_required
def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student')

    return render(request, "new_student.html", {'form': form})

@login_required
def update_student(request, id):
    student = Students.objects.get(s_id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student')

    return render(request, "new_student.html", {'form':form,'students': student})

@login_required()
def delete_student(request, id):
    student = Students.objects.get(s_id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student')

    return render(request, "confirmation.html", {'student':student})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            messages.success(request, "Password Changed Successfully!")
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            messages.error(request, "Failure")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "change_password.html", {'form':form})