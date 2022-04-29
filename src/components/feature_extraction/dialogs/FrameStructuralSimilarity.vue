<template>
  <div>
    <Dialog
      header="Frame Structural Similarity"
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
import struSimilarity from "../../../provider/struSimilarity";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "FrameStructuralSimilarity",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "ssresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        struSimilarity((data) => {
          ipcRenderer.send(ipcKeys.getResultTable, "structsimilarity");
        }, this.frmPath["VideoTitle"].split(".")[0]);
      }, 1000);
    },
  },
};
</script>
<style></style>
