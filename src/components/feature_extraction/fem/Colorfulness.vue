<template>
  <div>
    <Dialog
      header="Colorfulness"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="center"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="single-class">
          <RadioButton
            id="single"
            name="Single"
            value="0"
            v-model="selectedMode"
          />
          <label class="radio-label" for="single-frame">Single Frame</label>
        </div>
        <div class="pair-class">
          <RadioButton id="pair" name="Pair" value="1" v-model="selectedMode" />
          <label class="radio-label" for="pair-frame">Pair Frame</label>
        </div>
        <div class="p-col-3">
          <Button @click="onStart" label="Start" class="p-button-sm" />
        </div>
      </div>
    </Dialog>
  </div>
</template>
<script>
import colorFulness from "../../../provider/colorFulness";
import getProject from "../../../provider/getProject";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

let getProjectData;

export default {
  name: "Colorfulness",
  props: ["id"],
  data() {
    return {
      display: false,
      selectedMode: null,
      // colorfulness: [
      //   {
      //     name: "Hasler and Süsstrunk",
      //     value: 1,
      //   },
      // ],
    };
  },
  methods: {
    showModal() {
      this.display = true;
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      setTimeout(() => {
        colorFulness(
          (data) => {
            ipcRenderer.send(ipcKeys.getResultTable, "colorfulness");
          },
          this.selectedMode,
          getProjectData["VideoTitle"].split(".")[0]
        );
      }, 1000);
    },
  },

  mounted() {
    ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
    setTimeout(() => {
      getProject((data) => {
        getProjectData = data;
        ipcRenderer.send(ipcKeys.mainAppLoading, "stoploadfe");
        // ipcRenderer.send(ipcKeys.getGallary);
      }, this.$route.params.id);
    }, 1000);
  },
};
</script>
<style>
.single-class {
  padding-bottom: 5px;
}
.pair-class {
  padding-bottom: 25px;
}
</style>
