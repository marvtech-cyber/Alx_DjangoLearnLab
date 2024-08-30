from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from .models import Book

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
