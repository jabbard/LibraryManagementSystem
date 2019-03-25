from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Books)
admin.site.register(Book_Number)
admin.site.register(Students)
admin.site.register(Authors)
admin.site.register(Genres)
admin.site.register(Publishers)
#admin.site.register(Books_Authors)