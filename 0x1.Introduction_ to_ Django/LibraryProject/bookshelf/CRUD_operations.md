Create a Book instance:
from books.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
print(book)  
# Output: 1984 - George Orwell (1949)

Retrieve the book you created:
from books.models import Book
book = Book.objects.get(title='1984')
print("Title:", book.title)
print("Author:", book.author)
print("Publication Year:", book.publication_year)
# Output: [<Book: 1984 by George Orwell year 1949>]>

Update the title of the created book:
from books.models import Book
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
print(book.title)  
# Output: Nineteen Eighty-Four

Delete the book instance:
from books.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
print(Book.objects.all())  
# Output: [] (an empty list, confirming the book has been deleted)