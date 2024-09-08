from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    # The Meta class is used to define metadata about the serializer
    # The fields that should be included in the serialized data
    # "__all__" means all fields on the Book model will be included
     # The purpose of this serializer is to convert Book model instances to JSON data,
    # and to validate the data when it is deserialized (e.g., when creating a new book).
    # The validation method ensures that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        """
        # A custom validation method to check that the publication year is not in the future
        """
        if (data['publication_year']) > date.today().year:
            raise serializers.ValidationError("publication date can not be in the future")

class AuthorSerializer(serializers.ModelSerializer):
    """
    # The purpose of this serializer is to convert Author model instances to JSON data,
    # and to include the author's books in the serialized data.
    # The nested BookSerializer is used to serialize the author's books,
    # and the "read_only=True" argument ensures that the books field is read-only.
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']