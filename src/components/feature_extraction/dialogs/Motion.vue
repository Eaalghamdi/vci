<template>
  <div>
    <Dialog
      header="Motion"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="center"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-col-3">
          <Button @click="onStart" label="Start" class="p-button-sm" />
        </div>
      </div>
    </Dialog>
  </div>
</template>
<script>
import motion from "../../../provider/motion";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "Motion",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "moresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        motion((data) => {
          ipcRenderer.send(ipcKeys.getResultTable, "motion");
        }, this.frmPath["VideoTitle"]);
      }, 1000);
    },
  },
};
</script>
<style></style>
