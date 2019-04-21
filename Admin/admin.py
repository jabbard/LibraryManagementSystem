from django.contrib import admin
from .models import *
from .forms import BookForm



# Register your models here.
#admin.site.register(Books)
admin.site.register(Book_Number)
admin.site.register(Students)
admin.site.register(Authors)
admin.site.register(Genres)
admin.site.register(Publishers)
admin.site.register(Faculty)
admin.site.register(Transactions)
admin.site.register(Structures)
admin.site.register(Borrows)


admin.site.register(Books)
#admin.site.register(Books_Authors)

