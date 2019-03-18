from django.db import models

# Create your models here.
class Books(models.Model):
    book_id = models.CharField(primary_key=True, max_length=10)
    book_name = models.CharField(max_length=255, default="")
    ISBN = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    author = models.CharField(max_length=100, default="")
    publisher = models.CharField(max_length=255, default="")
    edition = models.CharField(max_length=255, default="")
    type_choices = (('Reference', 'Reference'),('Borrowable', 'Borrowable'))
    type = models.CharField(max_length=20, choices=type_choices, default="")
    genre = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.book_id