# recommendation.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .models import Book

def recommend_books(book, num_recommendations=3):
    input_embedding = book.embeddings
    print(f'book {book}')
    # Fetch all books with embeddings excluding the base book itself
    all_books = Book.objects.exclude(book_id=book.book_id).exclude(embeddings=None)

    product_embeddings = [eval(b.embeddings) for b in all_books]
    similarities = cosine_similarity([eval(input_embedding)], product_embeddings)[0]

    # Find the index of the most similar product
    most_similar_index = int(np.argmax(similarities))

    # Check if the similarity score for the most similar product is above a threshold
    threshold = 0.5  # Adjust this threshold as needed
    if similarities[most_similar_index] >= threshold:
        try:
            most_similar_product = all_books[most_similar_index]
        except IndexError:
            most_similar_product = None
    else:
        most_similar_product = None


    # Find the index of the recommended products (top N most similar)
    similarities[
        most_similar_index] = -1  # Set the similarity of the most similar product to -1 to find the next most similar
    num_recommendations = 3  # Change this value to get more or fewer recommendations
    recommended_indices = np.argsort(similarities)[-num_recommendations:]

    # Retrieve the recommended products from the database
    recommended_products = []
    for index in recommended_indices:
        try:
            recommended_product = all_books[int(index)]  # Convert index to int
            recommended_products.append(recommended_product)
        except IndexError:
            # Handle the case where the queryset is empty
            pass
    print('_________________-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(f'most_similar_product {most_similar_product}')
    print('_________________-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(f"recommended_products {recommended_products}")
    return recommended_products

    # Calculate similarity scores
    recommendations = []
    for book in all_books:
        target_embeddings = np.array(book.embeddings)
        similarity_score = 1 - cosine(base_embeddings, target_embeddings)
        recommendations.append((book, similarity_score))

    # Sort recommendations by similarity score in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Return top recommendations
    top_recommendations = recommendations[:num_recommendations]
    print(f'top_recommendations {top_recommendations}')
    return top_recommendations
