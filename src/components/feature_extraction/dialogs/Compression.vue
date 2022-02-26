<template>
  <div>
    <Dialog
      header="Compression"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="center"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <label class="title-thr">Select Format</label>
          <div class="list-item">
            <Dropdown
              v-model="selectFormat"
              :options="formatList"
              optionLabel="name"
              optionValue="value"
              placeholder="Select a Method"
            />
          </div>
          <label class="title-com">Resolution</label>

          <div class="thr-cl">
            <label class="title-com">Width</label>
            <InputNumber
              v-model="width"
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
          <div class="thr-cl">
            <label class="title-com">Height</label>
            <InputNumber
              v-model="height"
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
          <div class="thr-cl">
            <label class="title-com">FPS</label>
            <InputNumber
              v-model="fps"
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
        <div class="btn-comp">
          <Button @click="onStart" label="Start" class="p-button-sm" />
        </div>
      </div>
    </Dialog>
  </div>
</template>
<script>
import compression from "../../../provider/compression";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";

export default {
  name: "Compression",
  props: ["id", "frmPath"],
  data() {
    return {
      display: false,
      selectFormat: "",
      width: 450,
      height: 450,
      fps: 10,
      formatList: [
        { name: "MPG", value: 1 },
        { name: "MP4", value: 2 },
        { name: "M4V", value: 3 },
        { name: "AVI", value: 4 },
        { name: "WMV", value: 5 },
        { name: "MOV", value: 6 },
        { name: "FLV", value: 7 },
      ],
    };
  },
  methods: {
    showModal() {
      this.display = true;
      ipcRenderer.send(ipcKeys.panelVisibility, "coresultshow");
    },
    onStart() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      this.display = false;
      setTimeout(() => {
        compression(
          (data) => {
            ipcRenderer.send(ipcKeys.getResultTable, "compression");
          },
          this.frmPath["VideoTitle"],
          this.width,
          this.height,
          this.fps,
          this.formatList[this.selectFormat]["name"]
        );
      }, 1000);
    },
  },
};
</script>
<style>
.list-item {
  padding-top: 10px;
  padding-bottom: 20px;
}
.btn-comp {
  padding-top: 30px;
}
</style>
