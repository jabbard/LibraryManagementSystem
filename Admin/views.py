from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm, GenreForm, AuthorForm, PublisherForm, FacultyForm, StudentForm, SignupForm, IssueForm, ReturnForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def index(request):
    return render(request, "adminstrator/index.html")

@login_required
def books(request):
    book_list = Books.objects.all()
    return render(request, "adminstrator/tables.html", {'book_list': book_list})

@login_required
def add_books(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('book')

    return render(request, "adminstrator/new_book.html", {'form':form})

@login_required
def update_book(request, id):
    book = Books.objects.get(book_id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book')
    return render(request, "adminstrator/new_book.html", {'form':form, 'book':book})

@login_required
def delete_book(request, id):
    book = Books.objects.get(book_id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book')

    return render(request, "adminstrator/confirmation.html", {'book': book})

@login_required
def genres(request):
    genre_list = Genres.objects.all()
    return render(request, "adminstrator/genres.html", {'genre_list': genre_list})

@login_required
def add_genre(request):
    form = GenreForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('genre')

    return render(request, "adminstrator/new_genre.html", {'form': form})

@login_required
def update_genre(request, id):
    genre = Genres.objects.get(genre_id=id)
    form = GenreForm(request.POST or None, instance=genre)

    if form.is_valid():
        form.save()
        return redirect('genre')

    return render(request, "adminstrator/new_genre.html", {'form': form, 'genre': genre})

@login_required
def delete_genre(request, id):
    genre = Genres.objects.get(genre_id=id)

    if request.method == 'POST':
        genre.delete()
        return redirect('genre')

    return render(request, "adminstrator/confirmation.html", {'genre': genre})

@login_required
def authors(request):
    author = Authors.objects.all()

    return render(request,"adminstrator/authors.html", {'author':author})

@login_required
def add_author(request):
    form = AuthorForm(request.POST or None)
    authors = Authors.objects.filter(author_name=request.POST.get('author_name')).count()

    if authors == 0 and form.is_valid():
        form.save()
        return redirect('author')
    else:
        form = AuthorForm()
        messages.error(request,"The author with similar id or name already exists!")

    return render(request, "adminstrator/new_author.html", {'form':form})

@login_required
def update_author(request, id):
    author = Authors.objects.get(author_id=id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('author')

    return render(request,"adminstrator/new_author.html", {'form':form, 'author':author})

@login_required
def delete_author(request, id):
    authors = Authors.objects.get(author_id=id)

    if request.method == 'POST':
        authors.delete()
        return redirect('author')

    return render(request, "adminstrator/confirmation.html", {'author': authors})

@login_required
def publisher(request):
    publishers = Publishers.objects.all()

    return render(request, "adminstrator/publishers.html", {'publishers':publishers})

@login_required
def add_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('publisher')

    return render(request, "adminstrator/new_publisher.html", {'form':form})

@login_required
def update_publisher(request, id):
    publisher = Publishers.objects.get(publish_id=id)
    form = PublisherForm(request.POST or None, instance=publisher)

    if form.is_valid():
        form.save()
        return redirect('publisher')

    return render(request, "adminstrator/new_publisher.html", {'form':form, 'publishers':publisher})

@login_required
def delete_publisher(request, id):
    publisher = Publishers.objects.get(publish_id = id)
    if request.method == "POST":
        publisher.delete()
        return redirect('publisher')

    return render(request, "adminstrator/confirmation.html", {'publisher':publisher})

@login_required
def faculty(request):
    faculties = Faculty.objects.all()

    return render(request, "adminstrator/faculties.html", {'faculty':faculties})

@login_required
def add_faculty(request):
    form = FacultyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('faculty')

    return render(request, "adminstrator/new_faculty.html", {'form': form})

@login_required
def update_faculty(request, id):
    faculty = Faculty.objects.get(f_id=id)

    form = FacultyForm(request.POST or None, instance=faculty)

    if form.is_valid():
        form.save()
        return redirect('faculty')

    return render(request, "adminstrator/new_faculty.html", {'form': form, 'faculties': faculty})

@login_required
def delete_faculty(request,id):
    faculty = Faculty.objects.get(f_id=id)

    if request.method == "POST":
        faculty.delete()
        return redirect('faculty')

    return render(request, "adminstrator/confirmation.html", {'faculties': faculty})

@login_required
def student(request):
    student = Students.objects.all()

    return render(request,"adminstrator/students.html", {'students':student})

@login_required
def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student')

    return render(request, "adminstrator/new_student.html", {'form': form})

@login_required
def update_student(request, id):
    student = Students.objects.get(s_id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('student')

    return render(request, "adminstrator/new_student.html", {'form':form,'students': student})

@login_required()
def delete_student(request, id):
    student = Students.objects.get(s_id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student')

    return render(request, "adminstrator/confirmation.html", {'student':student})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            messages.success(request, "Password Changed Successfully!")
            form.save()
            #update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            messages.error(request, "Failure")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "adminstrator/change_password.html", {'form':form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'Thank you for using.')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user.is_superuser:
                login(request, user)
                return redirect('index')
            elif user.is_staff:
                login(request,user)
                return redirect('library')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'adminstrator/login.html',{'form':form})


def library_home(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library')
        else:
            return redirect('librarian/404.html')
    else:
        form = IssueForm()
    return render(request, 'librarian/homepage.html', {'form':form})

def register_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user = request.POST.get('username')
        userr = Students.objects.filter(s_id=user).count()
        if form.is_valid() and userr > 0:
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your library account'
            message = render_to_string('activation.html', {
                'user':user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return redirect('register')

    else:
        form = SignupForm()
    return render(request, 'adminstrator/register.html', {'form':form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('library')
    else:
        return HttpResponse('Activation link is invalid!')


def issue_book(request):
    if request.method == 'POST':
        st = request.POST.get('student_id')
        trans = Transactions.objects.filter(student_id=st)
        a=0
        for val in trans:
            if val.return_status==0:
                a=a+1
        book_id = request.POST.get('b_id')
        book1 = Book_Number.objects.get(b_id=book_id)
        book_num = book1.book_id
        book = Books.objects.get(book_id=book_num.book_id)


        form = IssueForm(request.POST)
        if form.is_valid() and a<2 and book.type=='Borrowable' and book1.status=='Available':
            form.save()
            book1.status='Taken'
            book1.save()
            return redirect('library')
        else:
            return redirect('issue')
    else:
        form = IssueForm()
    return render(request, 'librarian/issue_book.html', {'form':form})

def return_book(request):
    if request.method=='POST':
        form = ReturnForm(request.POST)
        obj = Transactions.objects.filter(b_id=request.POST.get('book_id')).filter(return_status=0)
        if form.is_valid() and obj.count()==1:
            objs = obj[0]
            objs.return_date = datetime.now()
            objs.return_status = 1
            objs.save()
            return redirect('library')
        else:
            raise ValueError('Book has been already returned!')
    else:
        form = ReturnForm()
    return render(request, 'librarian/return_book.html', {'form': form})
