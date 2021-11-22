import { createRouter, createWebHashHistory } from "vue-router";
import CreateProject from "../views/CreateProject.vue";
import MainApp from "../views/MainApp.vue";
import FeatureExtractionView from "../views/FeatureExtractionView.vue";
import VisualizationView from "../views/VisualizationView.vue";

const routes = [
  {
    path: "/",
    name: "CreateProject",
    component: CreateProject,
  },

  {
    path: "/project/:id",
    name: "toProject",
    props: true,
    component: MainApp,
  },

  {
    path: "/featureExtraction/:id",
    name: "ToFeatureExtraction",
    props: true,
    component: FeatureExtractionView,
  },

  {
    path: "/visualization/:id",
    name: "ToVisualization",
    props: true,
    component: VisualizationView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  mode: "history",
  routes,
});

export default router;
