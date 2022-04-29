<template>
  <div>
    <div style="text-align: right">
      <Button
        icon="pi pi-external-link"
        label="Export"
        @click="exportCSV()"
      />
    </div>
    <ScrollPanel style="height: 600px" class="custom">
      <DataTable :value="products" style="width: 1400px">
        <Column field="imgname" header="Image Name"></Column>
        <Column field="meanval" header="Mean Value"></Column>
        <Column field="stdval" header="Std Value"></Column>
        <Column field="meanadjabs" header="Mean Adj Abs"></Column>
        <Column field="stdadjabs" header="Std Adj Abs"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getEdgeDetection from "../../../provider/getEdgeDetection";
import toExcel from "../../../provider/toExcel";

export default {
  name: "EDResultTable",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    exportCSV() {
      toExcel(this.products, "edgedetection");
    },
  },
  mounted() {
    ipcRenderer.on(ipcKeys.getResultTableAck, (event, data) => {
      if (data == "edgedetection") {
        getEdgeDetection((data) => {
          this.products = data;
          console.log(data);
          ipcRenderer.send(ipcKeys.mainAppLoading, "stoploadfe");
        });
      }
    });
  },
};
</script>
<style scoped>
</style>
