<template>
  <Panel header="Recent Projects" :toggleable="true" class="mainPanel">
    <template #icons>
      <button class="p-panel-header-icon p-link p-mr-2" @click="deleteProject">
        <span class="pi pi-trash"></span>
      </button>
    </template>
    <div class="p-grid">
      <div id="projectsList" v-if="projects.length > 0">
        <div
          v-for="project in projects"
          :key="project.ProjectTitle"
          class="p-field-checkbox"
        >
          <Checkbox
            :id="project.id"
            name="project"
            :value="project.id"
            v-model="selectedProject"
          />

          <label :for="project">
            <div v-if="project.ProjectTitle.length < 20">
              <router-link
                id="projectItem"
                :to="{
                  name: 'mainApp',
                  params: {
                    id: project.id,
                    filePath: project.videoPath,
                    fileName: project.videoFileName,
                  },
                }"
              >
                {{ project.ProjectTitle }}
              </router-link>
            </div>

            <div v-else>
              <router-link
                id="projectItem"
                :to="{
                  name: 'mainApp',
                  params: {
                    id: project.id,
                    filePath: project.videoPath,
                    fileName: project.videoFileName,
                  },
                }"
              >
                {{
                  ".." +
                  project.ProjectTitle.substring(
                    project.ProjectTitle.length,
                    project.ProjectTitle.length / 1.6
                  )
                }}
              </router-link>
            </div>
          </label>
        </div>
      </div>
    </div>
  </Panel>
</template>
<script>
import deleteProject from "../../provider/deleteProject";
import getProjects from "../../provider/getProjects";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../utils/config";

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
    deleteProject() {
      // when project not selected but delete button has pressed show warning
      if (this.selectedProject.length == 0) {
        ipcRenderer.send(
          ipcKeys.newProFieldsEmpty,
          "Mark recent projects for delete"
        );
      } else if (this.selectedProject.length >= 1) {
        ipcRenderer.send(
          ipcKeys.delPro,
          "Are you sure you want to delete selected ?"
        );
        ipcRenderer.on(ipcKeys.delProConfirm, () => {
          ipcRenderer.removeListener(ipcKeys.newProCreatedSucc, () => {});
          ipcRenderer.send(ipcKeys.createProPageLoading, "loadnow");
          setTimeout(() => {
            deleteProject(
              this.selectedProject,
              (updatedData) => {
                console.log(updatedData.length);
                this.selectedProject = updatedData;
              },
              this.projects,
              () => {
                getProjects((data) => {
                  this.projects = data;
                  if (this.selectedProject.length == 0) {
                    ipcRenderer.send(ipcKeys.createProPageLoading, "stopload");
                  }
                });
              }
            );
          }, 1000);
        });
      }
    },
  },

  mounted() {
    getProjects((data) => (this.projects = data));
    ipcRenderer.on(ipcKeys.newProCreatedSucc, () => {
      getProjects((data) => (this.projects = data));
      ipcRenderer.removeListener(ipcKeys.newProCreatedSucc, () => {});
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

.p-grid {
  display: inline-flex;
}

.p-field-checkbox {
  padding-top: 7px;
  padding-bottom: 7px;
  display: flex;
}

.mainPanel {
  left: 35%;
  right: 35%;
  position: absolute;
}

#projectItem {
  padding-left: 20px;
  color: gray;
}
</style>
