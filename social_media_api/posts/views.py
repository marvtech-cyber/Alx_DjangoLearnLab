# Import the necessary modules from Django Rest Framework
from rest_framework import viewsets, permissions, filters, generics, status
# Import the DjangoFilterBackend for filtering
from django_filters.rest_framework import DjangoFilterBackend
# Import the Post, Comment, and Like models from the current app
from .models import Post, Comment, Like
# Import the PostSerializer and CommentSerializer from the current app
from .serializers import PostSerializer, CommentSerializer
# Import the custom permission class IsAuthorOrReadOnly from the current app
from .permissions import IsAuthorOrReadOnly
# Import the Response class from Django Rest Framework
from rest_framework.response import Response
# Import the action decorator from Django Rest Framework
from rest_framework.decorators import action

# Define a viewset for Post objects
class PostViewSet(viewsets.ModelViewSet):
    # Specify the queryset for the viewset
    queryset = Post.objects.all()
    # Specify the serializer class for the viewset
    serializer_class = PostSerializer
    # Specify the permission classes for the viewset
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    # Specify the filter backends for the viewset
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # Specify the search fields for the viewset
    search_fields = ['title', 'content']
    # Specify the filterset fields for the viewset
    filterset_fields = ['author']

    # Override the perform_create method to set the author of the post
    def perform_create(self, serializer):
        # Save the post with the current user as the author
        serializer.save(author=self.request.user)
        
  

# Define a viewset for Comment objects
class CommentViewSet(viewsets.ModelViewSet):
    # Specify the queryset for the viewset
    queryset = Comment.objects.all()
    # Specify the serializer class for the viewset
    serializer_class = CommentSerializer
    # Specify the permission classes for the viewset
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # Override the perform_create method to set the author of the comment
    def perform_create(self, serializer):
        # Save the comment with the current user as the author
        serializer.save(author=self.request.user)
        # Get the post associated with the comment
        post = Post.objects.get(pk=self.kwargs['post_pk'])
       


 