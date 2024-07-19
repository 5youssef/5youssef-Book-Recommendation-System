<!-- Vue.js Component Template -->
<template id="app-home">
  <div class="container mt-5">
      <h1 class="text-center mb-4">Welcome to Wiggli Challenge</h1>
      
      <div class="card">
          <div class="card-body">
              <h2 class="card-title">Book Recommendation System</h2>
              <h3 class="card-subtitle mb-3 text-muted">Objective</h3>
              <p class="card-text">
                  Create a book recommendation system based on book descriptions. Use the OpenAI API for processing book descriptions and Langchain for managing the processing pipeline. Data will be managed and analyzed with Pandas.
              </p>
              <h3 class="card-subtitle mb-3 text-muted">Steps</h3>
              <ol class="card-text">
                  <li>Collect Data: Use the Google Books API to retrieve book descriptions.</li>
                  <li>Prepare Data: Clean and store the data in a Pandas DataFrame.</li>
                  <li>Obtain Embeddings: Use the OpenAI API to obtain embeddings for the descriptions.</li>
                  <li>Create Processing Chain: Use Langchain to automate the processing flow.</li>
                  <li>Recommend Books: Implement a recommendation algorithm based on the similarity of embeddings.</li>
                  <li>Evaluate and Improve: Assess performance and suggest improvements.</li>
              </ol>
              <h3 class="card-subtitle mb-3 text-muted">Deliverables</h3>
              <ul class="card-text">
                  <li>Source Code: GitHub repository with the code.</li>
                  <li>Documentation: README with instructions and architecture.</li>
                  <li>Evaluation Report: Document explaining results and improvements.</li>
              </ul>
          </div>
      </div>
  </div>
</template>