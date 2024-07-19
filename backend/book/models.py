from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=200)
    book_id = models.CharField(max_length=200)
    authors = models.CharField(max_length=350)
    image_url = models.URLField(max_length=200, null=True)
    description = models.TextField()
    language = models.CharField(max_length=200)
    embeddings = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
