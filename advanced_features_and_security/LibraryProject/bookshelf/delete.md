from bookshelf.models import Book

delete_book = Book.objects.get (title = "Nineteen Eighty-Four")
delete_book.delete() (1, {'bookshelf.Book': 1})
print(Book.objects.all())  
# Output: [] (an empty list, confirming the book has been deleted)