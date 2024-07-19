import os
import requests
from .models import Book

OPENAI_API_KEY = "sk-proj-dPbm1I3pY9cKJUBKqgczT3BlbkFJL0U6Q71ZgfIi7CNCMgEj"  # Ensure your API key is set as an environment variable

def get_embeddings(text):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    body = {
      "model": "text-embedding-ada-002",
      "input": '{text}'
    }

    response = requests.post("https://api.openai.com/v1/embeddings", headers=headers, json=body)
    embeddings = response.json().get("data")[0].get("embedding")
    return embeddings 



def save_embeddings():
    books = Book.objects.all()
    for book in books:
        embeddings = get_embeddings(book.description)
        if embeddings:
            book.embeddings = embeddings
            book.save()
        else:
            print(f"Failed to retrieve embeddings for book: {book.title}")
    
    print("Embedding retrieval and update completed.")
