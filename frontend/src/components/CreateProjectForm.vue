<template>
  <div class="p-d-block">
    <form v-on:submit.prevent="onProjectCreate">
      <div class="p-fluid p-mb-2">
        <InputText
          id="projectName"
          v-model="projects.ProjectTitle"
          type="text"
          placeholder="Give it a name"
        />
      </div>

      <div class="p-inputgroup">
        <InputText
          id="videoURL"
          v-model="projects.VideoPath"
          placeholder="upload a video"
        />
        <Button
          @click="handleSaveChart"
          icon="pi pi-upload"
          class="p-button-warning"
        />
      </div>

      <div class="p-col-4">
        <Button label="Create" type="submit" />
      </div>
    </form>
  </div>
  <div v-if="loading" class="loading">
    <ProgressBar mode="indeterminate" style="height: 0.5em" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateProjectForm",

  data() {
    return {
      loading: false,
      projects: {
      },
    };
  },
  created() {
    const ipc = require("electron").ipcRenderer;
    ipc.on("save-finished", function (event, newProject) {
      this.projects = newProject
    });
  },

  methods: {
    handleSaveChart: function () {
      // Send a signal to the IPC channel, then the main thread receives the signal and immediately executes the corresponding response function
      const ipc = require("electron").ipcRenderer;
      ipc.send("open-file-upload-dialog");
    },

    onProjectCreate() {
      console.log(this.projects)
      this.loading = true;
      axios
        .post("http://127.0.0.1:8000/api/add_projects", this.projects)
        .then((res) => {
          this.loading = false;

          this.$router.push({ name: "toProject", params: { id: res.data } });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.loading {
  padding-top: 10px;
}
</style>
