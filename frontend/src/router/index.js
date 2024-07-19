import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import BookList from '../views/book/BookList'
import ShowBook from '../views/book/ShowBook'
import PageNotFound from '../views/PageNotFound'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/book',
    name: 'Book',
    component: BookList
  },
  {
    path: '/book/:book_id',
    name: 'post-show',
    component: ShowBook,
    props: true
  },
  {
    path: '/:catchAll(.*)',
    component: PageNotFound
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
