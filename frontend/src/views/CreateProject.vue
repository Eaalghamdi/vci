<template>
  <div class="p-grid startForm">
    <div class="p-col-4">
      <div v-if="error" class="error">
        {{ error }}
      </div>
      <h1>Start a New Project</h1>
      <CreateProjectForm />
    </div>
    <div class="p-col-4">
      <ProjectHistroy />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import CreateProjectForm from "@/components/CreateProjectForm.vue";
import ProjectHistroy from "@/components/ProjectHistroy.vue";

export default {
  name: "CreateProject",
  components: {
    CreateProjectForm,
    ProjectHistroy,
  },
};
</script>

<style scoped>
.startForm {
  display: felx;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 10vh;
}
</style>
