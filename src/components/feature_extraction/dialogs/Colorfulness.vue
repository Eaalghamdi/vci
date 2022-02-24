<template>
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
</template>
<script>
import colorFulness from "../../../provider/colorFulness";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "Colorfulness",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
      selectedMode: null,
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "cfresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        colorFulness(
          (data) => {
            ipcRenderer.send(ipcKeys.getResultTable, "colorfulness");
          },
          this.selectedMode,
          this.frmPath["VideoTitle"].split(".")[0]
        );
      }, 1000);
    },
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
