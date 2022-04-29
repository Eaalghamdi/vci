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
        <Column field="imgcolor" header="Image Color"></Column>
        <Column field="meancolor" header="Mean Color"></Column>
        <Column field="stdcolor" header="Std Color"></Column>
        <Column field="meanadj" header="Mean Adj"></Column>
        <Column field="stdadj" header="Std Adj"></Column>
        <Column field="meanadjabs" header="Mean Adj Abs"></Column>
        <Column field="stdadjabs" header="Std Adj Abs"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getcolorFulness from "../../../provider/getColorFulness";
import toExcel from "../../../provider/toExcel";

export default {
  name: "CFResultTable",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    exportCSV() {
      toExcel(this.products, "colorfulness");
    },
  },
  mounted() {
    ipcRenderer.on(ipcKeys.getResultTableAck, (event, data) => {
      if (data == "colorfulness") {
        getcolorFulness((data) => {
          this.products = data;
          ipcRenderer.send(ipcKeys.mainAppLoading, "stoploadfe");
        });
      }
    });
  },
};
</script>
<style scoped>
</style>
