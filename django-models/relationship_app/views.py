from typing import Any
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test


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
    

def loginview(request):
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
    
def logoutview(request):
    logout(request)
    return redirect('login_view')


def Admin_check(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(Admin_check)
def Admin_view(request):
    return render(request, 'admin_view.html')

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(member_check)
def member_view(request):
    return render(request, 'member_view.html')

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html')