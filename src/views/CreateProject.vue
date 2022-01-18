<template>
  <div>
    <loading
      v-model:active="isLoading"
      :can-cancel="false"
      :is-full-page="fullPage"
      :color="color"
      :background-color="bgColor"
      :loader="loaderDesgin"
      :opacity="opacity"
    />
    <div class="p-grid">
      <div class="p-col-4">
        <h1>Start a New Project</h1>
      </div>
      <div class="p-col-4">
        <CreateProjectForm />
      </div>
      <div class="p-col-4">
        <ProjectHistroy />
      </div>
    </div>
  </div>
</template>

<script>
import CreateProjectForm from "../components/create_project/CreateProjectForm.vue";
import ProjectHistroy from "../components/create_project/ProjectHistroy.vue";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../utils/config";

export default {
  name: "CreateProject",
  data() {
    return {
      isLoading: false,
      fullPage: true,
      color: "#ff8c00",
      bgColor: "#1a1a1a",
      loaderDesgin: "dots",
      opacity: 0.85,
    };
  },
  components: {
    Loading,
    CreateProjectForm,
    ProjectHistroy,
  },

  mounted() {
    ipcRenderer.on(ipcKeys.creProPgeLoadAck, (event, data) => {
      if (data == "loadnow") {
        this.isLoading = true;
      } else {
        this.isLoading = false;
      }
    });
  },
};
</script>

<style scoped>
.p-grid {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 10vh;
}
</style>
