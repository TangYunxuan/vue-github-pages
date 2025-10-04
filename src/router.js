import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Thoughts from '@/views/Thoughts.vue'
import Projects from '@/views/Projects.vue'
import Travels from '@/views/Travels.vue'
import Cute from '@/views/Cute.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/thoughts', component: Thoughts },
  { path: '/projects', component: Projects },
  { path: '/travels', component: Travels },
  { path: '/cute', component: Cute }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router