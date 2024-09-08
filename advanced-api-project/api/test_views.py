from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

class BookTests(APITestCase):
    """
    Test cases for the Book API.
    """

    def setUp(self):
        """
        Set up the test data.
        """
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year=2023, author=self.author)
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        """
        Test creating a new book.
        Purpose: Test creating a new book.
        Input: A JSON payload with title, publication year, and author ID.
        Expected Output: A 201 Created response with the newly created book's ID, and the book count should be incremented by 1.
        Assertions:
            Response status code is 201 Created.
            Book count is incremented by 1.
            Newly created book's title matches the input title.
        """
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Book')

    def test_read_book(self):
        """
        Test reading an existing book.
        
        Purpose: Test reading an existing book.
        Input: A GET request to the book detail URL.
        Expected Output: A 200 OK response with the book's details.
        Assertions:
            Response status code is 200 OK.
            Book's title matches the expected title.
        """
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        """
        Test updating an existing book.
        Purpose: Test updating an existing book.
        Input: A PATCH request to the book detail URL with updated title.
        Expected Output: A 200 OK response with the updated book's details.
        Assertions:
            Response status code is 200 OK.
            Book's title matches the updated title.
        """
        data = {'title': 'Updated Book Title'}
        response = self.client.patch(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.id).title, 'Updated Book Title')

    def test_delete_book(self):
        """
        Test deleting an existing book.
        Purpose: Test deleting an existing book.
        Input: A DELETE request to the book detail URL.
        Expected Output: A 204 No Content response, and the book count should be decremented by 1.
        Assertions:
            Response status code is 204 No Content.
            Book count is decremented by 1.
        """
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """
        Test filtering books by title.
        Purpose: Test filtering books by title.
        Input: A GET request to the book list URL with title filter parameter.
        Expected Output: A 200 OK response with a list of books matching the filter.
        Assertions:
            Response status code is 200 OK.
            List of books contains only one book with the expected title.
        """
        response = self.client.get(self.book_list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')

    def test_search_books(self):
        """
        Test searching books by keyword.
        Purpose: Test searching books by keyword.
        Input: A GET request to the book list URL with search parameter.
        Expected Output: A 200 OK response with a list of books matching the search keyword.
        Assertions:
            Response status code is 200 OK.
            List of books contains only one book with the expected title.
        """
        response = self.client.get(self.book_list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books(self):
        """
        Test ordering books by publication year.
        Purpose: Test ordering books by publication year.
        Input: A GET request to the book list URL with ordering parameter.
        Expected Output: A 200 OK response with a list of books ordered by publication year.
        Assertions:
            Response status code is 200 OK.
            List of books contains the expected book at the first position.
        """
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')

    def test_permissions(self):
        """
        Test permission checks for unauthorized access.
        Purpose: Test permission checks for unauthorized access.
        Input: A GET request to the book list URL without authentication.
        Expected Output: A 403 Forbidden response.
        Assertions:
        Response status code is 403 Forbidden.
        """
        # Log out the user to test permissions
        self.client.logout()
        
        self.client.credentials()  # Remove authentication
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)