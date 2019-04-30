from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm, GenreForm, AuthorForm, PublisherForm, FacultyForm, StudentForm, SignupForm, IssueForm, \
    ReturnForm, StructuresForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import admin_only, staff_only
from django.conf import settings
import datetime
from django.db.models import Q

@login_required
@admin_only
def index(request):
    no = Book_Number.objects.all().count()
    taken = Book_Number.objects.filter(status='Taken').count()
    inside = no - taken
    transaction = Transactions.objects.filter(return_status=0).prefetch_related('student_id').prefetch_related('b_id')
    return render(request, "adminstrator/index.html",{
        'no':no,
        'taken':taken,
        'inside':inside,
        'transaction':transaction,
    })

@login_required
@admin_only
def books(request):
    book_list = Books.objects.all()
    storage = messages.get_messages(request)
    return render(request, "adminstrator/tables.html", {'book_list': book_list, 'message' : storage})

@login_required
@admin_only
def add_books(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "The book has been added succesfully.", extra_tags='alert')
        return redirect('book')

    return render(request, "adminstrator/new_book.html", {'form':form})

@login_required
def update_book(request, id):
    if User.is_superuser:
        book = Books.objects.get(book_id=id)
        form = BookForm(data=request.POST or None, instance=book)

        if form.is_valid():
            form.save()
            messages.info(request, "The book has been modified.", extra_tags='alert')
            return redirect('book')
        return render(request, "adminstrator/new_book.html", {'form':form, 'book':book})
    else:
        raise PermissionError

@login_required
def delete_book(request, id):
    if User.is_superuser:
        book = Books.objects.get(book_id=id)

        if request.method == 'POST':
            book.delete()
            messages.error(request, "The book has been deleted.", extra_tags='alert')
            return redirect('book')

        return render(request, "adminstrator/confirmation.html", {'book': book})
    else:
        raise PermissionError

@login_required
@admin_only
def genres(request):
    genre_list = Genres.objects.all()
    return render(request, "adminstrator/genres.html", {'genre_list': genre_list})

@login_required
def add_genre(request):
    if User.is_superuser:
        form = GenreForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('genre')

        return render(request, "adminstrator/new_genre.html", {'form': form})
    else:
        raise PermissionError

@login_required
def update_genre(request, id):
    if User.is_superuser:
        genre = Genres.objects.get(genre_id=id)
        form = GenreForm(request.POST or None, instance=genre)

        if form.is_valid():
            form.save()
            return redirect('genre')

        return render(request, "adminstrator/new_genre.html", {'form': form, 'genre': genre})
    else:
        raise PermissionError

@login_required
def delete_genre(request, id):
    if User.is_superuser:

        genre = Genres.objects.get(genre_id=id)

        if request.method == 'POST':
            genre.delete()
            return redirect('genre')

        return render(request, "adminstrator/confirmation.html", {'genre': genre})
    else:
        raise PermissionError

@login_required
@admin_only
def authors(request):
    author = Authors.objects.all()

    return render(request,"adminstrator/authors.html", {'author':author})

@login_required
@admin_only
def add_author(request):
    form = AuthorForm(request.POST or None)
    authors = Authors.objects.filter(author_name=request.POST.get('author_name')).count()

    if authors == 0 and form.is_valid():
        form.save()
        return redirect('author')
    else:
        form = AuthorForm()

    return render(request, "adminstrator/new_author.html", {'form':form})

@login_required
def update_author(request, id):
    if User.is_superuser:
        author = Authors.objects.get(author_id=id)
        form = AuthorForm(request.POST or None, instance=author)

        if form.is_valid():
            form.save()
            return redirect('author')

        return render(request,"adminstrator/new_author.html", {'form':form, 'author':author})
    else:
        raise PermissionError
@login_required
def delete_author(request, id):
    if User.is_superuser:

        authors = Authors.objects.get(author_id=id)

        if request.method == 'POST':
            authors.delete()
            return redirect('author')

        return render(request, "adminstrator/confirmation.html", {'author': authors})
    else:
        raise PermissionError

@login_required
@admin_only
def publisher(request):
    publishers = Publishers.objects.all()

    return render(request, "adminstrator/publishers.html", {'publishers':publishers})

@login_required
@admin_only
def add_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('publisher')

    return render(request, "adminstrator/new_publisher.html", {'form':form})

@login_required
def update_publisher(request, id):
    if User.is_superuser:
        publisher = Publishers.objects.get(publish_id=id)
        form = PublisherForm(request.POST or None, instance=publisher)

        if form.is_valid():
            form.save()
            return redirect('publisher')

        return render(request, "adminstrator/new_publisher.html", {'form':form, 'publishers':publisher})
    else:
        raise PermissionError

@login_required
def delete_publisher(request, id):
    if User.is_superuser:

        publisher = Publishers.objects.get(publish_id = id)
        if request.method == "POST":
            publisher.delete()
            return redirect('publisher')

        return render(request, "adminstrator/confirmation.html", {'publisher':publisher})
    else:
        raise PermissionError


@login_required
@admin_only
def faculty(request):
    faculties = Faculty.objects.all()

    return render(request, "adminstrator/faculties.html", {'faculty':faculties})

@login_required
@admin_only
def add_faculty(request):
    form = FacultyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('faculty')

    return render(request, "adminstrator/new_faculty.html", {'form': form})

@login_required
def update_faculty(request, id):
    if User.is_superuser:

        faculty = Faculty.objects.get(f_id=id)

        form = FacultyForm(request.POST or None, instance=faculty)

        if form.is_valid():
            form.save()
            return redirect('faculty')

        return render(request, "adminstrator/new_faculty.html", {'form': form, 'faculties': faculty})
    else:
        raise PermissionError

@login_required
def delete_faculty(request,id):
    if User.is_superuser:
        faculty = Faculty.objects.get(f_id=id)

        if request.method == "POST":
            faculty.delete()
            return redirect('faculty')

        return render(request, "adminstrator/confirmation.html", {'faculties': faculty})
    else:
        raise PermissionError

@login_required
@admin_only
def student(request):
    student = Students.objects.all()

    return render(request,"adminstrator/students.html", {'students':student})

@login_required
@admin_only
def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student')

    return render(request, "adminstrator/new_student.html", {'form': form})

@login_required
def update_student(request, id):
    if User.is_superuser:
        student = Students.objects.get(s_id=id)
        form = StudentForm(request.POST or None, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student')

        return render(request, "adminstrator/new_student.html", {'form':form,'students': student})
    else:
        raise PermissionError

@login_required
def delete_student(request, id):
    if User.is_superuser:
        student = Students.objects.get(s_id=id)

        if request.method == 'POST':
            student.delete()
            return redirect('student')

        return render(request, "adminstrator/confirmation.html", {'student':student})
    else:
        raise PermissionError

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            messages.success(request, "Password Changed Successfully!", extra_tags='alert')
            form.save()
            #update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            messages.error(request, "Failure")
            return redirect('change_password')
    else:

        form = PasswordChangeForm(user=request.user)
        return render(request, "adminstrator/change_password.html", {'form':form})\

@login_required
def change_librarian_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            messages.success(request, "Password Changed Successfully!", extra_tags='alert')
            form.save()
            #update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            messages.error(request, "Failure")
            return redirect('change_password')
    else:

        form = PasswordChangeForm(user=request.user)
        return render(request, "librarian/change_password.html", {'form':form})



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
            elif user.is_staff and not user.is_superuser:
                login(request,user)
                deadline_tomorrow = Transactions.objects.filter(return_date = datetime.date.today()+datetime.timedelta(days=1))
                email = [tom.student_id.email for tom in deadline_tomorrow]
                book = [tom.b_id.book_id.book_name for tom in deadline_tomorrow]

                if len(email)>0:
                    for e in email:
                        subject = 'Reminder!'
                        book_name = book[email.index(e)]
                        email_from = settings.EMAIL_HOST_USER
                        to = [e,]
                        message = 'Dear {},\nPlease return {} book tomorrow or the next working day.'.format(e,book_name)
                        send_mail(subject, message, email_from, to)

                return redirect('library')

    else:
        form = AuthenticationForm()
        return render(request,'adminstrator/login.html',{'form':form})

@login_required
def library_home(request):
    transaction = Transactions.objects.filter(return_status=0).prefetch_related('student_id').prefetch_related('b_id')
    storage = messages.get_messages(request)
    counter = Borrows.objects.filter(Q(validation_status=0) | Q(validation_status=2))
    count = counter.filter(seen_status=0).count
    return render(request, "librarian/homepage.html", {'transaction': transaction, 'messages':storage, 'count':count,})

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
        return redirect('student')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def issue_book(request):
    if request.method == 'POST':
        st = request.POST.get('student_id')
        trans = Transactions.objects.filter(student_id=st)
        a = 0
        for val in trans:
            if val.return_status==0:
                a=a+1
        book_id = request.POST.get('b_id')
        book1 = Book_Number.objects.get(b_id=book_id)
        book_num = book1.book_id
        book = Books.objects.get(book_id=book_num.book_id)
        available = False
        if (book1.status == 'Available'):
            available = True
        elif (book1.status == 'Borrowed'):
            st_id = Borrows.objects.filter(st_id=st)
            is_valid = st_id.filter(validation_status=1)
            for valid in is_valid:
                if(book1.book_id==valid.book_id):
                    available=True
            if not available:
                messages.error(request, "This book is reserved.", extra_tags='alert')
        is_student = Students.objects.get(s_id=st)


        form = IssueForm(request.POST)
        if form.is_valid() and a < (Structures.objects.latest('no_of_books').no_of_books) and book.type=='Borrowable' \
            and available and is_student:
            Transactions.objects.create(student_id=Students.objects.get(s_id=st), b_id=Book_Number.objects.get(b_id=book_id))
            a = book.count
            book.count = a-1
            book.save()
            book1.status='Taken'
            book1.save()
            messages.success(request, "The books has been lended.", extra_tags='alert')
            return redirect('library')
        else:
            if(a>=Structures.objects.latest('no_of_books').no_of_books):
                messages.error(request,"The student has borrowed the maximum number of books.", extra_tags='alert')
                return redirect('issue')
            elif(book.type != 'Borrowable'):
                messages.error(request, "The book is a reference book and thus it cant be borrowed.", extra_tags='alert')
                return redirect('issue')
            elif(book1.status == 'Taken'):
                messages.error(request, "The book is not available or has not been returned in the system",
                               extra_tags='alert')
                return redirect('issue')
            elif(available):
                messages.error(request,"The Student ID does not belong to any student.", extra_tags='alert')
            return redirect('issue')
    else:
        storage = messages.get_messages(request)
        form = IssueForm()
        return render(request, 'librarian/issue_book.html', {'form':form, 'storage':messages})

@login_required
def return_book(request):
    if request.method=='POST':
        form = ReturnForm(request.POST)
        book_id = request.POST.get('book_id')
        obj = Transactions.objects.filter(return_status=0)
        books = Book_Number.objects.get(b_id=book_id)
        bookID = books.book_id
        book = Books.objects.get(book_id=bookID.book_id)
        if form.is_valid() and obj.filter(b_id=book_id).count() == 1:
            objs = obj[0]
            days = datetime.datetime.today() - objs.return_date.replace(tzinfo=None)
            if days.days > Structures.objects.latest('days').days:
                fine = Structures.objects.all()
                messages.warning(request,"The book submitted is "+days+"late and the student has to pay"+(fine[len(fine)-1]*days), extra_tags='alert')
            else:
                messages.success(request,"The book has been returned.", extra_tags='alert')
            a = book.count
            book.count = a+1
            book.save()
            objs.return_date = datetime.date.today()
            objs.return_status = 1
            books.status = 'Available'
            books.save()
            objs.save()
            return redirect('library')
        else:
            raise ValueError('Book has been already returned!')
    else:
        form = ReturnForm()
    return render(request, 'librarian/return_book.html', {'form': form})

@admin_only
@login_required
def barcodes(request):
    num = Book_Number.objects.all().prefetch_related('book_id')
    return render(request, "adminstrator/barcode_book.html", {'num':num})

@admin_only
@login_required
def transactions(request):
    transaction = Transactions.objects.filter(return_status=0).prefetch_related('student_id').prefetch_related('b_id')

    return render(request, "adminstrator/transaction.html", {'transaction':transaction})

@admin_only
@login_required
def structure(request):
    structure = Structures.objects.all()
    this_structure = structure.latest('date')

    return render(request, "adminstrator/structures.html", {'structure':this_structure})

@admin_only
@login_required
def update_structures(request):
    if request.method == 'POST':
        form = StructuresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure')
    else:
        form = StructuresForm()
    return render(request, "adminstrator/update_structures.html", {'form':form})

def student(request):
    books = Books.objects.all()[:3]
    count = 0
    if request.user.is_authenticated:
        user_count = Transactions.objects.filter(student_id=request.user.username)
        count = user_count.filter(return_status=0).count()
    return render(request, "student/home.html", {'books':books, 'num': count})

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('student')
    form = AuthenticationForm()
    return render(request,"student/login.html", {'form':form})

@login_required(login_url='student_login')
def borrow(request, id):
    #storage = messages.get_messages(request)
    student_id = Students.objects.get(s_id=request.user.username)
    book_id = Books.objects.get(book_id=id)
    time = datetime.datetime.now()
    if time.time() > datetime.time(17,0,0,0) or time.weekday() == 4:
        Borrows.objects.create(st_id=student_id,book_id=book_id,valid_till=time.timedelta(days=2))
    else:
        Borrows.objects.create(st_id = student_id, book_id=book_id)
    return redirect('student')

@login_required
def borrowal_page(request):
    storage = messages.get_messages(request)
    list = Borrows.objects.filter(validation_status=0)
    accepted_list = Borrows.objects.filter(validation_status=1)
    expiry_list = accepted_list.filter(valid_till__lte=datetime.datetime.today())
    for a in expiry_list:
        a.book_id.count = a.book_id.count + 1
        a.validation_status = 2
        a.save()
    for lists in list:
        lists.seen_status=1
        lists.save()
    return render(request, "librarian/borrowal.html", {'list':list, 'messages':storage})

@login_required
def accept_borrowal(request, pk):
    borrow = Borrows.objects.get(pk=pk)
    book = borrow.book_id.book_id
    count = Books.objects.get(book_id=book)
    st_filter = Transactions.objects.filter(student_id=borrow.st_id.s_id)
    st_count = st_filter.filter(return_status=0).count()
    if(borrow.valid_till.replace(tzinfo=None) > datetime.datetime.today().replace(tzinfo=None) and count.count>0 and st_count < Structures.objects.latest('no_of_books').no_of_books):
        borrow.validation_status = 1
        borrow.valid_till = datetime.datetime.today()+datetime.timedelta(days=1)
        borrow.save()
        book = borrow.book_id.book_id
        barcode = Book_Number.objects.filter(book_id=book)
        available_book = barcode.filter(status='Available')
        if(available_book):mdc
            available_book.status = 'Borrowed'
            available_book.save()
        count = Books.objects.get(book_id=book)
        count.count = count.count - 1
        count.save()
        messages.success(request, "Success", extra_tags='alert')
        subject = 'Your borrow request has been accepted!'
        book_name = borrow.book_id.book_name
        email_from = settings.EMAIL_HOST_USER
        to = [borrow.st_id.email, ]
        message = 'Dear {},\nYour request to borrow {} book has been accepted.\nPlease visit the library to collect the aforementioned book.'.format(borrow.st_id.first_name, book_name)
        send_mail(subject, message, email_from, to)

        return redirect('borrowing')
    else:
        messages.error(request,"The borrow request has expired.",extra_tags='alert')

@login_required
def decline_borrowal(request, pk):
    borrowal = Borrows.objects.get(pk=pk)
    borrowal.validation_status = 2
    borrowal.save()
    messages.error(request, "The borrow request has been rejected.", extra_tags='alert')
    return redirect('borrowing')





