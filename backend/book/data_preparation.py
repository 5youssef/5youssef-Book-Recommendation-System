import os
import requests
import pandas as pd
from django.conf import settings
from book.models import Book
from .data_collection import fetch_book_data


def prepare_data_and_save():
    books = fetch_book_data()
    # Prepare data using Pandas DataFrame
    data = []
    for book in books:
        book_id = book['id']
        title = book['volumeInfo'].get('title')
        image_url = book['volumeInfo'].get('imageLinks', {}).get('thumbnail') or book['volumeInfo'].get('imageLinks', {}).get('smallThumbnail')
        language = book['volumeInfo'].get('language')
        authors = book['volumeInfo'].get('authors')
        description = book['volumeInfo'].get('description')
        data.append({'book_id': book_id, 'title':title, 'description': description, 'image_url': image_url, 'language': language, 'authors': authors})

    # Convert to DataFrame
    df = pd.DataFrame(data)
    print(f'df {df}')

    # Clean data if needed (e.g., remove duplicates, handle missing values)
    df.drop_duplicates(subset=['book_id'], inplace=True)
    
    #Clean data: Remove rows where description is null or empty
    df = df.dropna(subset=['description'])  # Drop rows where description is NaN or None



    # Save to Django model
    for index, row in df.iterrows():
        Book.objects.update_or_create(book_id=row['book_id'], defaults={'title': row['title'], 'description': row['description'], 'authors': row['authors'], 'image_url': row['image_url'], 'language': row['language']})

