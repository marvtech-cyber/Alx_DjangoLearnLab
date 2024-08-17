from bookshelf.models import Book 
retrieve_book = Book.objects.get(title = "1984") print(retrieve_book)
print("Title:", book.title)
print("Author:", book.author)
print("Publication Year:", book.publication_year)


# Output: [<Book: 1984 by George Orwell year 1949>]>