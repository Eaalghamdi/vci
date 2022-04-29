<template>
  <div>
    <div style="text-align: right">
      <Button icon="pi pi-external-link" label="Export" @click="exportCSV()" />
    </div>
    <ScrollPanel style="height: 600px" class="custom">
      <DataTable :value="products" style="width: 1000px">
        <Column field="filename" header="File Name"></Column>
        <Column field="numfaces" header="No of Facess"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getFaceDetection from "../../../provider/getFaceDetection";
import toExcel from "../../../provider/toExcel";

export default {
  name: "FDResultTable",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    exportCSV() {
      toExcel(this.products, "facedetection");
    },
  },
  mounted() {
    ipcRenderer.on(ipcKeys.getResultTableAck, (event, data) => {
      if (data == "facedetection") {
        getFaceDetection((data) => {
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
