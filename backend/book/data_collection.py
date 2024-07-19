import os
import requests
from django.conf import settings
from .models import Book

API_KEY = "AIzaSyCMpY_fOJGE3Fwydo-GIO_md1rCO21xV6c"
QUERY = "fiction books"
URL = f"https://www.googleapis.com/books/v1/volumes?q={QUERY}&key={API_KEY}"

def fetch_book_data():
    response = requests.get(URL)
    if response.status_code == 200:
        books = response.json().get('items', [])
        return books
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def save_to_db(books):
    for book in books:
        book_id = book['id']
        title = book['volumeInfo'].get('title')
        image_url = book['volumeInfo'].book['imageLinks'].get('thumbnail')
        language = book['volumeInfo'].get('language')
        authors = book['volumeInfo'].get('authors')
        description = book['volumeInfo'].get('description', 'No description')
        Book.objects.create(book_id=book_id, title=title, description=description,  authors=authors, image_url=image_url, language=language)


