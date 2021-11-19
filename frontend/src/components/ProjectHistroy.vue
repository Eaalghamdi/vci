<template>
  <Panel header="Recent Projects">
    <div class="p-d-block">
      <div id="projectsList" v-if="projects.length > 0">
        <div v-for="project in projects" :key="project.title">
          <router-link
            :to="{
              name: 'toProject',
              params: { id: project.id },
            }"
          >
            <h3 id="projectItem">{{ project.title }}</h3>
          </router-link>
        </div>
      </div>
    </div>
  </Panel>
</template>
<script>
import axios from "axios";
export default {
  name: "ProjectHistroy",
  data() {
    return {
      selectedProject: null,
      projects: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8001/api/all_projects")
      .then((response) => {
        this.projects = response.data;
        console.log(this.projects);
      })
      .catch(function(error) {
        console.log(error);
      });
  },
};
</script>
<style scoped>
.p-listbox {
  background: #1e1e1e;
  color: rgba(255, 255, 255, 0.87);
  border: 0px solid #383838;
  border-radius: 3px;
}

#projectItem {
  color: gray;
}
</style>
