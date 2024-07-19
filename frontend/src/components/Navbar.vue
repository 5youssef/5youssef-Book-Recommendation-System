<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <a class="navbar-brand" href="#">Wiggli</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor01">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link class="nav-link" :to="{ name: 'Home' }">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Book' }">Book</router-link>
        </li>
      </ul>
    </div>
  </nav>
  <div class="my-3">
    <button @click="fetchData" class="btn btn-success ml-2">Fetch Data</button>
  </div>
</template>
<script>
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'Navbar',
  setup() {
    const router = useRouter();

    const fetchData = () => {
      fetch('http://localhost:8000/api/fetch-data/') 
        .then(response => response.json())
        .then(data => {
          console.log('Data fetched:', data);
          router.push({ name: 'Book' });
        })
        .catch(err => console.error('Error fetching data:', err));
    };

    return {
      fetchData
    };
  }
});
</script>
