<template>
  <Dialog
    header="Sailency"
    v-model:visible="display"
    baseZIndex="999"
    autoZIndex="false"
    position="center"
  >
    <div class="p-col-3">
      <Button @click="onStart" label="Start" class="p-button-sm" />
    </div>
  </Dialog>
</template>
<script>
import motion from "../../../provider/motion";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "Sailency",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "saresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        motion((data) => {
          ipcRenderer.send(ipcKeys.getResultTable, "saliency");
        }, this.frmPath["VideoTitle"]);
      }, 1000);
    },
  },
};
</script>
<style></style>
