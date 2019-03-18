from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.home, name="home"),
    path('index', user_views.index, name="index"),
    path('books', user_views.books, name="book"),
    path('new_book', user_views.add_books, name="add_books"),
    path('update_book/<slug:id>', user_views.update_book, name="update_book"),
    path('delete_book/<slug:id>', user_views.delete_book, name="delete_book"),
    path('admin_login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
]