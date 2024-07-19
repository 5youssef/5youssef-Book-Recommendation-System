<template>
    <div>
      <div class="jumbotron">
        <div v-if="book">
          <h1 class="display-3">{{ book.title }}</h1>
          <p class="lead">by {{ book.authors }}</p>
          <hr class="my-4">
          <img :src="book.image_url" alt="Book cover" class="img-fluid mb-3">
          <p class="lead">{{ book.description }}</p>
          <p class="text-muted">Language: {{ book.language }}</p>
        </div>
        <div v-else class="text-center">Loading ...</div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-6" v-for="recommendation in recommendations" :key="recommendation.id">
            <div class="card mb-3">
              <div class="card-body">
                <h5 class="card-title">{{ recommendation.title }}</h5>
                <p class="card-text">{{ recommendation.description }}</p>
                <router-link :to="{ name: 'post-show', params: { book_id: recommendation.book_id }}">
                  <button class="btn btn-primary">View Details</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import { ref, watch, onMounted } from 'vue';
import { useRoute } from 'vue-router';

export default {
  setup() {
    const route = useRoute();
    const book = ref(null);
    const recommendations = ref([]);

    const fetchBookDetails = () => {
      fetch(`http://localhost:8000/api/book/${route.params.book_id}/recommendations/`)
        .then(res => res.json())
        .then(data => {
          book.value = data.book;
          recommendations.value = data.recommendations;
        })
        .catch(err => console.log(err));
    };

    watch(() => route.params.book_id, fetchBookDetails);

    onMounted(() => {
      fetchBookDetails();
    });

    return {
      book,
      recommendations
    };
  }
};
</script>
  