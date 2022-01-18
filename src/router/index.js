import { createRouter, createWebHashHistory } from 'vue-router'
import CreateProject from '../views/CreateProject.vue'
import MainApp from '../views/MainApp.vue'

const routes = [
  {
    path: '/',
    name: 'createProject',
    component: CreateProject
  },
  { 
    path: '/mainapp/:id',
    name: 'mainApp',
    props: true,
    component: MainApp
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
