from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Books(models.Model):
    book_id = models.CharField(primary_key=True, max_length=10)
    book_name = models.CharField(max_length=255, default="")
    isbn_regex = RegexValidator(regex='^[0-9]{10}|[0-9]{13}$', message="The ISBN number should be 10 or 13 digit in length.")
    ISBN = models.CharField(validators=[isbn_regex],max_length=100, default="")
    description = models.TextField(default="")
    author = models.CharField(max_length=100, default="")
    publisher = models.CharField(max_length=255, default="")
    edition = models.CharField(max_length=255, default="")
    type_choices = (('Reference', 'Reference'),('Borrowable', 'Borrowable'))
    type = models.CharField(max_length=20, choices=type_choices, default="")
    genre = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.book_id

class Book_Number(models.Model):
    b_id = models.CharField(primary_key=True, max_length=10)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.b_id

class Faculty(models.Model):
    f_id = models.CharField(primary_key=True, max_length=10)
    f_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.f_id

class Students(models.Model):
    s_id = models.CharField(primary_key=True, max_length=10)
    st_name = models.CharField(max_length=100, default="")
    ph_validator = RegexValidator(regex='^(98[0-9]{8}|97[0-9]{8})', message="Invalid Phone no.")
    ph_num = models.CharField(validators=[ph_validator],max_length=15, default="")
    email_validator = RegexValidator(regex='^([\w]*[\w\.]*(?!\.)@islingtoncollege.edu.np)', message="Invalid email address!")
    email = models.EmailField(validators=[email_validator],default="")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_id


