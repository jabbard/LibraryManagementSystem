from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.
class Authors(models.Model):
    author_id = models.AutoField(primary_key=True, max_length=10)
    author_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.author_id)

class Publishers(models.Model):
    publish_id = models.AutoField(primary_key=True, max_length=10)
    publisher_name = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.publish_id)

class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True, max_length=10)
    genre_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.genre_id)

class Books(models.Model):
    book_id = models.AutoField(primary_key=True, max_length=10)
    book_name = models.CharField(max_length=255, default="")
    isbn_regex = RegexValidator(regex='^[0-9]{10}|[0-9]{13}$', message="The ISBN number should be 10 or 13 digit in length.")
    ISBN = models.CharField(validators=[isbn_regex],max_length=100, default="")
    description = models.TextField(default="")
    #author = models.CharField(max_length=100, default="")
    publisher = models.ForeignKey(Publishers, on_delete=models.SET_NULL, null=True)
    edition = models.CharField(max_length=255, default="")
    type_choices = (('Reference', 'Reference'),('Borrowable', 'Borrowable'))
    type = models.CharField(max_length=20, choices=type_choices, default="")
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.book_id)


class Books_Authors(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, default="")
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE, default="")

    def __str__(self):
        return str(id)

class Book_Number(models.Model):
    b_id = models.CharField(primary_key=True, max_length=10)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.b_id

class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True, max_length=10)
    f_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.f_id)

class Students(models.Model):
    s_id = models.CharField(primary_key=True, max_length=10)
    st_name = models.CharField(max_length=100, default="")
    ph_validator = RegexValidator(regex='^(98[0-9]{8}|97[0-9]{8})', message="Invalid Phone no.")
    ph_num = models.CharField(validators=[ph_validator],max_length=15, default="")
    email_validator = RegexValidator(regex='^([\w]*[\w\.]*(?!\.)@islingtoncollege.edu.np)', message="Invalid email address!")
    email = models.EmailField(validators=[email_validator],default="")
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.s_id

class Transactions(models.Model):
    sn = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.SET_NULL, null=True)
    b_id = models.ForeignKey(Book_Number, on_delete=models.SET_NULL, null=True)
    issued_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.sn)

