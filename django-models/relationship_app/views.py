from typing import Any
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

#function based view to list all books
def list_books(request):

    # fetch all books from database
    books = Book.objects.all()

    # context dictionary with book list
    context = {'list_books': books}

    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """
    a class-based view  that displays details for a specific library,
      listing all books available in that library.
    """

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        else:
            form = UserCreationForm()
            context = {'form: form'}

        return render(request, 'relationship_app/register.html', context)
    

def login_view(request):
    if request.method == 'POST':
        form =AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            else:
                return "Invalid credentials"
        else:
            form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'login.html', context)
    
def logout_view(request):
    logout(request)
    return redirect('login_view')