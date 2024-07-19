from django.urls import path
from .views import *

urlpatterns = [
    path('books/', all_books_api, name='all_books_api'),
    path('fetch-data/', fetch_data, name='fetch_data'),
    path('book/<str:book_id>/recommendations/', book_recommendations_api, name='book_recommendations_api'),
    # Other URL patterns
]
