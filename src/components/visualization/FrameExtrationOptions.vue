<template>
  <div class="stepsdemo-content">
    <Card>
      <template #title> Plot Information </template>
      <template #content>
        <div class="p-fluid p-formgrid p-grid">
          <div class="p-field p-col-12 p-md-6">
            <label for="class">Class</label>
            <Dropdown
              v-model="selecFunc"
              :options="funcList"
              optionLabel="name"
              optionValue="value"
              placeholder="Select a Method"
            />
          </div>
          <div class="p-field p-col-12 p-md-6">
            <label for="lastname">Chart Type</label>
            <Dropdown
              v-model="selecPlot"
              :options="plotList"
              optionLabel="name"
              optionValue="value"
              placeholder="Select a Plot"
            />
          </div>
        </div>
      </template>
      <template #footer>
        <div class="p-grid p-nogutter p-justify-between">
          <Button @click="onSubmit" class="create_btn" label="Submit" />
        </div>
      </template>
    </Card>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../utils/config";

export default {
  name: "FrameExtraxtionOoptions",
    props: ["id", "filePath", "fileName"],
  data() {
    return {
      selecFunc: "",
      funcList: [
        { name: "Object Recognition", value: 1 },
        { name: "Colorfulness", value: 2 },
        { name: "Structural Similarity", value: 3 },
        { name: "Compression", value: 4 },
        { name: "Face Recognition", value: 5 },
        { name: "Edge Detecion", value: 6 },
        { name: "Motion", value: 7 },
        { name: "Sailency", value: 8 },
      ],
      selecPlot: "",
      plotList: [
        { name: "Bar Chart", value: 1 },
        { name: "Line Chart", value: 2 },
      ],
    };
  },

  methods: {
    onSubmit() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadVis");
      if (this.selecFunc == 1) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showORPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 2) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showCFPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 3) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showSSPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 4) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showCOPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 5) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showFDPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 6) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showEDPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 7) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showMOPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      } else if (this.selecFunc == 8) {
        ipcRenderer.send(ipcKeys.panelVisibility, [
          "showSAPlan",
          this.selecPlot == 1 ? "bar" : "line",
        ]);
      }
    },
  },
};
</script>
<style scoped></style>
