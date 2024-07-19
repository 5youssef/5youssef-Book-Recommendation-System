# Book Recommendation System

A project to create a book recommendation system based on book descriptions. This system uses the OpenAI API for processing book descriptions and Langchain for managing the processing pipeline. Data is managed and analyzed with Pandas.

## Technologies

1. [Google Books API](https://developers.google.com/books/docs/v1/getting_started) - For retrieving book descriptions
2. [Pandas](https://pandas.pydata.org/) - For data cleaning and storage
3. [OpenAI API](https://beta.openai.com/docs/) - For obtaining embeddings for the book descriptions
5. [Docker](https://docs.docker.com/engine/install/) & Docker Compose - For containerization



## Run Project

### Prerequisites

1. Create a `.env` file in the project root and add the necessary environment variables:
   - `OPENAI_API_KEY` - Your OpenAI API key
   - `GOOGLE_BOOKS_API_KEY` - Your Google Books API key

### Steps to Run

1. **Launch Docker**

2. **Build and Run Containers**

   ```shell
   docker compose up --build
