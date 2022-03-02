<template>
  <div>
    <div style="text-align: right">
      <Button icon="pi pi-external-link" label="Export" @click="exportCSV()" />
    </div>
    <ScrollPanel style="height: 600px" class="custom">
      <DataTable :value="products" style="width: 1300px">
        <Column field="filename" header="File Name"></Column>
        <Column field="mean" header="Mean"></Column>
        <Column field="std" header="STD"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getSliency from "../../../provider/getSliency";
import toExcel from "../../../provider/toExcel";

export default {
  name: "SAResultTable",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    exportCSV() {
      toExcel(this.products, "saliency");
    },
  },
  mounted() {
    ipcRenderer.on(ipcKeys.getResultTableAck, (event, data) => {
      if (data == "saliency") {
        getSliency((data) => {
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
