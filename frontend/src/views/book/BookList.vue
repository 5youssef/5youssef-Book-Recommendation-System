<script>
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const books = ref([]);

    const fetchRecommendations = () => {
      fetch('http://localhost:8000/api/books/') // Adjust endpoint to your backend API
        .then(res => res.json())
        .then(data => {
          books.value = data;
          console.log(books.value);
        })
        .catch(err => console.error('Error fetching recommendations:', err));
    };

    onMounted(() => {
      fetchRecommendations();
    });

    return {
      books
    };
  }
};
</script>
<template>
  <div>
    <div class="jumbotron">
      <h1 class="display-3">Book Recommendations</h1>
      <p class="lead">Browse through our recommended books.</p>
      <hr class="my-4">
      <p>Explore and discover your next read.</p>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-md-6" v-for="book in books" :key="book.id">
          <div class="card mb-3">
            <div class="card-body">
              <h1 class="display-3">{{ book.title }}</h1>
              <p class="lead">by {{ book.authors }}</p>
              <hr class="my-4">
              <img :src="book.image_url" alt="Book cover" class="img-fluid mb-3">
              <p class="text-muted">Language: {{ book.language }}</p>                
              <router-link :to="{ name: 'post-show', params: { book_id: book.book_id }}">
                <button class="btn btn-primary">View Details</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
