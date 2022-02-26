<template>
  <div>
    <Dialog
      header="Object Detection"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="center"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <div class="p-field p-grid">
            <label for="firstname" class="p-col-fixed" style="width: 100px">
              Threshold</label
            >
            <div class="thr-cl">
              <InputNumber
                v-model="value1"
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
          </div>
        </div>

        <div class="start-btn">
          <Button @click="onStart" label="Start" class="p-button-sm" />
        </div>
      </div>
    </Dialog>
  </div>
</template>
<script>
import objectDetection from "../../../provider/objectDetection";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "ObjectDetection",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
      value1: 0.5,
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "odresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        objectDetection(
          (data) => {
            ipcRenderer.send(ipcKeys.getResultTable, "objectdetection");
          },
          this.frmPath["VideoTitle"].split(".")[0],
          this.value1
        );
      }, 1000);
    },
  },
};
</script>
<style>
.thr-cl {
  padding-top: 10px;
}
.start-btn {
  padding-top: 40px;
}
</style>
