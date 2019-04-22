from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User



# Create your models here.

class Authors(models.Model):
    author_id = models.CharField(primary_key=True, max_length=10)
    author_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.author_name

class Publishers(models.Model):
    publish_id = models.CharField(primary_key=True, max_length=10)
    publisher_name = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.publisher_name

class Genres(models.Model):
    genre_id = models.CharField(primary_key=True, max_length=10)
    genre_name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.genre_name

class Books(models.Model):
    book_id = models.CharField(primary_key=True, max_length=10)
    book_name = models.CharField(max_length=255, default="")
    isbn_regex = RegexValidator(regex='^[0-9]{10}|[0-9]{13}$', message="The ISBN number should be 10 or 13 digit in length.")
    ISBN = models.CharField(validators=[isbn_regex],max_length=100, default="")
    description = models.TextField(default="")
    author = models.ManyToManyField(Authors, related_name='author')
    publisher = models.ForeignKey(Publishers, on_delete=models.SET_NULL, null=True)
    edition = models.CharField(max_length=255, default="")
    type_choices = (('Reference', 'Reference'),('Borrowable', 'Borrowable'))
    type = models.CharField(max_length=20, choices=type_choices, default="")
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name


"""class Books_Authors(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, default="")
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(id)"""

class Book_Number(models.Model):
    b_id = models.CharField(primary_key=True, max_length=10)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    status_choices = (('Available','Available'),('Taken','Taken'),('Borrowed','Borrowed'))
    status = models.CharField(choices=status_choices, default="", max_length=20)

    def __str__(self):
        return self.b_id

class Faculty(models.Model):
    f_id = models.CharField(primary_key=True, max_length=10)
    f_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.f_name

class Students(models.Model):
    s_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    ph_validator = RegexValidator(regex='^(98[0-9]{8}|97[0-9]{8})', message="Invalid Phone no.")
    ph_num = models.CharField(validators=[ph_validator],max_length=15, default="")
    email_validator = RegexValidator(regex='^([\w]*[\w\.]*(?!\.)@islingtoncollege.edu.np)', message="Invalid email address!")
    email = models.EmailField(validators=[email_validator],default="")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Transactions(models.Model):
    sn = models.BigAutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    b_id = models.ForeignKey(Book_Number, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(default=datetime.date.today())
    return_date = models.DateTimeField(default=datetime.date.today() + datetime.timedelta(days=10))
    return_status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.sn)

class Structures(models.Model):
    days = models.IntegerField(default=10, max_length=2)
    fine = models.IntegerField(default=5, max_length=2)
    no_of_books = models.IntegerField(default=2, max_length=1)
    date = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return str(self.days)+" "+str(self.fine)

class Borrows(models.Model):
    st_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(default=datetime.date.today())
    valid_till = models.DateTimeField(default=datetime.date.today() + datetime.timedelta(days=1))
    validation_status = models.IntegerField(max_length=1, default=0)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    seen_status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.st_id)+" "+str(self.book_id)

