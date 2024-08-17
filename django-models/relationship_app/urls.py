from . views import list_books, LibraryDetailView
from django.urls import path
from. import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]