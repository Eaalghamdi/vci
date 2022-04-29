<template>
  <div>
    <div style="text-align: right">
      <Button icon="pi pi-external-link" label="Export" @click="exportCSV()" />
    </div>
    <ScrollPanel style="height: 600px" class="custom">
      <DataTable :value="products" style="width: 1000px">
        <Column field="imganame" header="Image Name A"></Column>
        <Column field="imgbname" header="Image Name B"></Column>
        <Column field="mse" header="MSE"></Column>
        <Column field="ssim" header="SSIM"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getStruSimilarity from "../../../provider/getStruSimilarity";
import toExcel from "../../../provider/toExcel";

export default {
  name: "SSResultTable",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    exportCSV() {
      toExcel(this.products, "strcturalsaliency");
    },
  },
  mounted() {
    ipcRenderer.on(ipcKeys.getResultTableAck, (event, data) => {
      if (data == "structsimilarity") {
        getStruSimilarity((data) => {
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
