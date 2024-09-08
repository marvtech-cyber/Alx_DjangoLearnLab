from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']




class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    
    def post(self, request, *args, **kwargs):
        # Retrieve all books validates before creating
        publication_year = request.data.get('publication_year')
        if publication_year and int(publication_year) > datetime.now().year:
            return Response(
                {"error": "The publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.create(request, *args, **kwargs)

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # update the book model
    def put(self, request, *args, **kwargs):
        publication_year = request.data.get('publication_year')
        if publication_year and int(publication_year) > datetime.now().year:
            return Response(
                {"error": "The publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.update(request, *args, **kwargs)



class DetailView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # get all books

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # deletes book by retrieving book based on the primary key in the url
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

