
from django.contrib import admin
from django.urls import path
from relationship_app.views import LibraryDetailView, book_listView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library-detailed-view'),
    path('books/', book_listView, name='book-list'),
    
]
