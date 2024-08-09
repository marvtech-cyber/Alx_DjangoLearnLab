Create a Book instance:
from books.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
print(book)  
# Output: 1984 - George Orwell (1949)