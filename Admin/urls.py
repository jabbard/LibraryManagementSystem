from django.urls import path
from . import views as user_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', user_views.index, name="index"),
    path('books/', user_views.books, name="book"),
    path('books/new_book/', user_views.add_books, name="add_books"),
    path('books/update_book/<slug:id>', user_views.update_book, name="update_book"),
    path('books/delete_book/<slug:id>', user_views.delete_book, name="delete_book"),
    path('login/', user_views.login_view, name="login"),
    path('logout/', user_views.logout_view, name="logout"),
    path('genres/', user_views.genres, name="genre"),
    path('genres/add_genre/', user_views.add_genre, name="add_genre"),
    path('genres/update_genre/<slug:id>', user_views.update_genre, name="update_genre"),
    path('genres/delete_genre/<slug:id>', user_views.delete_genre, name="delete_genre"),
    path('authors/', user_views.authors, name="author"),
    path('authors/add_author/', user_views.add_author, name="add_author"),
    path('authors/update_author/<slug:id>', user_views.update_author, name="update_author"),
    path('authors/delete_author/<slug:id>', user_views.delete_author, name="delete_author"),
    path('publishers/', user_views.publisher, name="publisher"),
    path('publishers/add_publisher/', user_views.add_publisher, name="add_publisher"),
    path('publishers/update_publisher/<slug:id>', user_views.update_publisher, name="update_publisher"),
    path('publishers/delete_publisher/<slug:id>', user_views.delete_publisher, name="delete_publisher"),
    path('faculties/', user_views.faculty, name="faculty"),
    path('faculties/add_faculty/', user_views.add_faculty, name="add_faculty"),
    path('faculties/update_faculty/<slug:id>', user_views.update_faculty, name="update_faculty"),
    path('faculties/delete_faculty/<slug:id>', user_views.delete_faculty, name="delete_faculty"),
    path('students/', user_views.student, name="student"),
    path('students/add_student/', user_views.add_student, name="add_student"),
    path('students/update_student/<slug:id>', user_views.update_student, name="update_student"),
    path('students/delete_student/<slug:id>', user_views.delete_student, name="delete_student"),
    path('change_password/', user_views.change_password, name="change_password"),
    path('change_password_librarian/', user_views.change_librarian_password, name="change_librarian_password"),
    path('home/', user_views.library_home, name="library"),
    path('register/', user_views.register_view, name="register"),
    path('issue_book/', user_views.issue_book, name="issue"),
    path('return_book/', user_views.return_book, name="return"),
    path('barcode_num/', user_views.barcodes, name="barcode"),
    path('transactions/', user_views.transactions, name="transaction"),
    path('structures/', user_views.structure, name="structure"),
    path('students/', user_views.student, name="student"),
    path('update_structures/', user_views.update_structures, name="update_structure"),
    path('student_login/', user_views.student_login, name="student_login"),
    path('borrow/<slug:id>/', user_views.borrow, name="borrow"),
    path('borrowals/', user_views.borrowal_page, name="borrowing"),
    path('accept_borrowal/<slug:pk>', user_views.accept_borrowal, name="accept_borrow"),
    path('decline_borrowal/<slug:pk>', user_views.decline_borrowal, name="decline_borrow"),
    #path('accept_borrow/<slug:pk>', user_views.student_logout, name="student_logout"),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', user_views.activate, name="activate"),
]