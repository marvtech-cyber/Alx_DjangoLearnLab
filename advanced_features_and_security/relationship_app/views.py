from typing import Any
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect


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




#Checks if user is Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

#Checks if user is Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)

def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#Checks if user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Implement adding a book here
    if request.method == 'POST':
        # Process form data
        pass
    else:
        # Render form
        pass
    return render(request, 'add_book.html') 

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Process form data to update the book
        pass
    else:
        # Render form with book data
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  
    else:
        return render(request, 'delete_book.html', {'book': book})
    