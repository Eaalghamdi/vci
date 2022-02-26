<template>
  <div>
    <div style="text-align: right">
      <Button
        icon="pi pi-external-link"
        label="Export"
        @click="exportCSV($event)"
      />
    </div>
    <ScrollPanel style="height: 600px" class="custom">
      <DataTable :value="products" style="width: 1000px">
        <Column field="id" header="Id"></Column>
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

export default {
  name: "FDResultTable",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    exportCSV() {
      this.$refs.dt.exportCSV();
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
