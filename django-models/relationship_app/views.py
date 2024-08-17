from typing import Any
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

#function based view to list all books
def book_listView(request):

    # fetch all books from database
    books = books.objects.all()

    # context dictionary with book list
    context = {'book_list': books}

    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """
    a class-based view  that displays details for a specific library,
      listing all books available in that library.
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'