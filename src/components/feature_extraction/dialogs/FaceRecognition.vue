<template>
  <div>
    <Dialog
      header="Face Recognition"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="center"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="thr-gorup-b">
          <label class="title-thr">Min Neighbour</label>
          <InputNumber
            v-model="value"
            showButtons
            buttonLayout="horizontal"
            decrementButtonClass="p-button-danger"
            incrementButtonClass="p-button-success"
            incrementButtonIcon="pi pi-plus"
            decrementButtonIcon="pi pi-minus"
            mode="decimal"
            class="input-thr"
          />
        </div>

        <div class="button-start">
          <Button @click="onStart" label="Start" class="p-button-sm" />
        </div>
      </div>
    </Dialog>
  </div>
</template>
<script>
import faceDetection from "../../../provider/faceDetection";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "FaceRecognition",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
      value: 10,
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "fdresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        faceDetection(
          (data) => {
            ipcRenderer.send(ipcKeys.getResultTable, "facedetection");
          },
          this.frmPath["VideoTitle"].split(".")[0],
          this.value
        );
      }, 1000);
    },
  },
};
</script>
<style></style>
