from .views import LibraryDetailView
from django.urls import path
from .views import list_books
from. import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/<pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('logout/', views.LogoutView.as_view(template_name="logout")),
    path('login/', views.LogoutView.as_view(template_name="login")),
]

