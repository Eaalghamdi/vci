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
      <DataTable :value="products" style="width: 1400px">
        <Column field="filename" header="File Name"></Column>
        <Column field="cnvformat" header="Converted Format"></Column>
        <Column field="sizebytprev" header="Previus Size (Bytes)"></Column>
        <Column field="sizebytnew" header="Converted Size (Bytes)"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getCompression from "../../../provider/getCompression";

export default {
  name: "COResultTable",
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
      if (data == "compression") {
        getCompression((data) => {
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
