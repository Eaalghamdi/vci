<template>
  <div class="p-d-block">
    <div class="p-fluid p-mb-2">
      <InputText
        id="projectName"
        v-model="projectTitle"
        type="text"
        placeholder="Give it a name"
      />
    </div>
    <div class="p-inputgroup">
      <InputText
        id="videoURL"
        v-model="videoFileName"
        placeholder="upload a video"
      />
      <Button
        @click="handleUploadVideo"
        icon="pi pi-upload"
        class="p-button-warning"
      />
    </div>
    <div class="p-col-4">
      <Button @click="handleProjectCreate" class="create_btn" label="Create" />
    </div>
  </div>
</template>

<script>
import createProject from "../../provider/createProject";
import { ipcKeys, prefKeys } from "../../utils/config";
import { prefs } from "../../utils/prefs";
import { ipcRenderer } from "electron";
import getProject from "../../provider/getProject";

export default {
  name: "CreateProjectForm",

  data() {
    return {
      projects: {},
      videoFileName: "",
      projectTitle: "",
    };
  },
  mounted() {
    // get the selected file name when the video has picked through dialog
    ipcRenderer.on(ipcKeys.uplVidStatAck, (event, dats) => {
      this.videoFileName = prefs(prefKeys.selVideoFileName);
      ipcRenderer.removeListener(ipcKeys.uplVidStatAck, () => {});
    });
  },

  methods: {
    handleUploadVideo() {
      //open dialog for pick video
      ipcRenderer.send(ipcKeys.openVidUpDialog);
    },

    //store video file details to the database
    handleProjectCreate() {
      var selVideoFileName = prefs(prefKeys.selVideoFileName);
      var selVideoPath = prefs(prefKeys.selVideoPath);

      if (
        (this.projectTitle == "") &
        (selVideoFileName == undefined) &
        (selVideoPath == undefined)
      ) {
        ipcRenderer.send(ipcKeys.newProFieldsEmpty, "Fields cannot be empty");
      } else if (this.projectTitle == "") {
        ipcRenderer.send(ipcKeys.newProFieldsEmpty, "Enter project title");
      } else if (
        (selVideoFileName == undefined) &
        (selVideoPath == undefined)
      ) {
        ipcRenderer.send(ipcKeys.newProFieldsEmpty, "Pick a video");
      } else {
        //show loading spinner
        ipcRenderer.send(ipcKeys.createProPageLoading, "loadnow");
        setTimeout(() => {
          createProject((data) => {
            // if any error while create project alert user with msg
            if (data["error"] == "true") {
              ipcRenderer.send(ipcKeys.newProFieldsEmpty, data["data"]);
              this.videoFileName = "";
              //hide loading spinner
              ipcRenderer.send(ipcKeys.createProPageLoading, "stopload");
            } else {
              this.videoFileName = "";
              this.projectTitle = "";
              ipcRenderer.send(ipcKeys.newProCreatedSucc);

              // if project created successfuly then redirect to next page
              ipcRenderer.on(ipcKeys.newProCreatedSucc, () => {
                ipcRenderer.removeListener(ipcKeys.newProCreatedSucc, () => {});

                getProject((subData) => {
                  ipcRenderer.send(ipcKeys.createProPageLoading, "stopload");
                  this.$router.push({
                    name: "mainApp",
                    params: {
                      id: data["data"],
                      filePath: subData["VideoPath"],
                      fileName: subData["VideoTitle"],
                    },
                  });
                }, data["data"]);
              });
            }
          }, this.projectTitle);
        }, 1000);
      }
    },
  },
};
</script>

<style scoped>
.p-mb-2 {
  padding-top: 10px;
}
.p-inputgroup {
  padding-top: 10px;
}
.p-col-4 {
  padding-top: 20px;
  padding-bottom: 30px;
  display: flex;
  width: 100%;
}
.create_btn {
  position: relative;
  left: 32%;
}
</style>
