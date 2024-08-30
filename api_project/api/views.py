from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializers = BookSerializer
