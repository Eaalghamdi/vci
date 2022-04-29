<template>
  <Dialog
    header="Edge Detection"
    v-model:visible="display"
    baseZIndex="999"
    autoZIndex="false"
    position="center"
  >
    <div class="p-field p-col-12">
      <label class="title">Static Sailency</label>
      <div class="method-sel">
        <Dropdown
          v-model="selectedStatic"
          :options="staticSaliencyMethods"
          optionLabel="name"
          optionValue="value"
          placeholder="Select a Method"
        />
        <div v-if="selectedStatic == 3">
          <div class="thr-gorup-a">
            <label class="title-thr">Threshold 1</label>
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
          <div class="thr-gorup-b">
            <label class="title-thr">Threshold 2</label>
            <InputNumber
              v-model="value2"
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
      <div class="button-start">
        <Button @click="onStart" label="Start" class="p-button-sm" />
      </div>
    </div>
  </Dialog>
</template>
<script>
import edgeDetection from "../../../provider/edgeDetection";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "EdgeDetection",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
      selectedStatic: "",
      value1: 50,
      value2: 50,
      staticSaliencyMethods: [
        { name: "Spectral Residual", value: 1 },
        { name: "Saliency Fine Grained", value: 2 },
        { name: "Canny Edge Detection", value: 3 },
      ],
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "edresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        edgeDetection(
          (data) => {
            ipcRenderer.send(ipcKeys.getResultTable, "edgedetection");
          },
          this.frmPath["VideoTitle"].split(".")[0],
          "static",
          this.selectedStatic == 1
            ? "spectral"
            : this.selectedStatic == 2
            ? "finegrained"
            : this.selectedStatic == 3
            ? "canny"
            : "",
          this.value1,
          this.value2
        );
      }, 1000);
    },
  },
};
</script>
<style>
.method-sel {
  padding-top: 15px;
}
.button-start {
  padding-top: 15px;
}
.thr-gorup-a {
  padding-top: 15px;
  padding-bottom: 15px;
}
.input-thr {
  padding-top: 10px;
}
.thr-gorup-b {
  padding-bottom: 15px;
}
</style>
