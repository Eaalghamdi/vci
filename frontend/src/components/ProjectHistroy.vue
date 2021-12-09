<template>
  <Panel header="Recent Projects" :toggleable="true">
      <template #icons>
        <button class="p-panel-header-icon p-link p-mr-2" @click="deleteProject">
            <span class="pi pi-trash"></span>
        </button>
      </template> 
    <div class="p-grid">
      <div id="projectsList" v-if="projects.length > 0">
        <div v-for="project in projects" :key="project.ProjectTitle" class="p-field-checkbox" >
            <Checkbox :id="project.id" name="project" :value="project.id" v-model="selectedProject" />
              <label :for="project" >
          <router-link id="projectItem"
            :to="{
              name: 'toProject',
              params: { id: project.id },
            }"
          >
              {{ project.ProjectTitle }}
    
          </router-link>
            </label> 
     
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
      checked: false,
      selectedProject: [],
      projects: [],
    };
  },
  methods: {
    deleteProject () {
      axios
        .delete("http://127.0.0.1:8000/api/projects/delete", this.selectedProject)
        .catch((err) => {
          console.log(err);
        })
      this.selectedProject = null;
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/all_projects")
      .then((response) => {
        this.projects = response.data;
       
      })
      .catch((error) =>{
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

.delete_btn {
  float: right;

}
</style>
