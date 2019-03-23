from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.index, name="index"),
    path('books/', user_views.books, name="book"),
    path('new_book/', user_views.add_books, name="add_books"),
    path('update_book/<slug:id>', user_views.update_book, name="update_book"),
    path('delete_book/<slug:id>', user_views.delete_book, name="delete_book"),
    path('admin_login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('genre/', user_views.genres, name="genre"),
    path('add_genre/', user_views.add_genre, name="add_genre"),
    path('update_genre/<slug:id>', user_views.update_genre, name="update_genre"),
    path('delete_genre/<slug:id>', user_views.delete_genre, name="delete_genre"),
    path('authors/', user_views.authors, name="author"),
    path('add_author/', user_views.add_author, name="add_author"),
    path('update_author/<slug:id>', user_views.update_author, name="update_author"),
    path('delete_author/<slug:id>', user_views.delete_author, name="delete_author"),
    path('publisher/', user_views.publisher, name="publisher"),
    path('add_publisher/', user_views.add_publisher, name="add_publisher"),
    path('update_publisher/<slug:id>', user_views.update_publisher, name="update_publisher"),
    path('delete_publisher/<slug:id>', user_views.delete_publisher, name="delete_publisher"),
]