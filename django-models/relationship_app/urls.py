from .views import LibraryDetailView
from django.urls import path
from .views import list_books
from . import views
from.views import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('logout/', views.LogoutView.as_view(template_name="templates/logout.html")),
    path('login/', views.LoginView.as_view(template_name="templates/login.html")),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
]

