import { createRouter, createWebHashHistory } from 'vue-router'
import CreateProject from '../views/CreateProject.vue'
import MainApp from '../views/MainApp.vue'
import FeatureExtraction from '../views/FeatureExtraction.vue'
import Visualization from '../views/Visualization.vue'

const routes = [
  {
    path: '/',
    name: 'createProject',
    component: CreateProject
  },
  {
    path: '/mainapp/:id/:filePath/:fileName',
    name: 'mainApp',
    props: true,
    component: MainApp
  },
  {
    path: '/feauextraction/:id/:filePath/:fileName',
    name: 'featureExtraction',
    props: true,
    component: FeatureExtraction
  },
  {
    path: '/visualization/:id/:filePath/:fileName',
    name: 'visualization',
    props: true,
    component: Visualization
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
