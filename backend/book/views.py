from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .data_preparation import prepare_data_and_save
from .embedding_retrieval import save_embeddings 
from django.shortcuts import render, get_object_or_404
from .models import Book
from .recommendation import recommend_books
from .serializers import BookSerializer


import asyncio

async def save_embeddings_async():
    # Assume this function is asynchronous
    await save_embeddings()
    
@api_view(['GET'])
def fetch_data(request):
    try:
        prepare_data_and_save()
        save_embeddings()
        return Response({"message": "Data fetched and saved successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def all_books_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_recommendations_api(request, book_id):
    print(f"Received request for book recommendations with book_id: {book_id}")
    book = get_object_or_404(Book, book_id=book_id)
    num_recommendations = 3
    recommendations = recommend_books(book, num_recommendations)
    serializer_book = BookSerializer(book)
    serializer_recommendations = BookSerializer(recommendations, many=True)
    
    return Response({
        'book': serializer_book.data,
        'recommendations': serializer_recommendations.data
    })
