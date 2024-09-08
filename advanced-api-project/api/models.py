from django.db import models

class Author(models.Model):
    
    """
    # The author's name, stored as a character field with a maximum length of 50 characters
    # The purpose of this model is to store information about individual authors.
    # Each author has a unique name, and this model allows us to store and retrieve that information.
    """
    name = models.CharField(max_length=50)



class Book(models.Model):
    """
    # The title of the book, stored as a character field with a maximum length of 100 characters.
    # The year of publication, stored as an integer field.
    # The author of the book, stored as a foreign key that references the Author model
    # The on_delete=models.CASCADE argument means that if the associated author is deleted, all books written by that author will also be deleted.
    # The related_name='books' argument allows us to access all books written by an author using the 'books' attribute on the Author instance.
    # The purpose of this model is to store information about individual books.
    # Each book has a title, a year of publication, and an author, and this model allows us to store and retrieve that information.
    """
    title = models.CharField(max_length=100)
    publication = models.IntegerField()
    author = models.ForeignKey(Author,on_delete= models.CASCADE, related_name='books' )
    
