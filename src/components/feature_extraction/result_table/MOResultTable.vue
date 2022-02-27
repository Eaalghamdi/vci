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
      <DataTable :value="products" style="width: 1800px">
        <Column field="id" header="Id"></Column>
        <Column field="videoname" header="Video Name"></Column>
        <Column
          field="numberofmovingobjects"
          header="Number of Moving Objects"
        ></Column>
        <Column
          field="movingdurationms"
          header="Moving Duration (m/s)"
        ></Column>
        <Column
          field="ratioofmovingobjectsns"
          header="Ratio of Moving Objects (ns)"
        ></Column>
        <Column
          field="ratioofmovingobjectsnm"
          header="Ratio of Moving Objects (nm)"
        ></Column>
        <Column
          field="movingdurtiondifferencemean"
          header="Moving Durtion Difference Mean"
        ></Column>
        <Column
          field="movingdurtiondifferencevaraince"
          header="Moving Durtion Difference Varaince"
        ></Column>
        <Column
          field="movingdurtiondifferencesd"
          header="Moving Durtion Difference sd"
        ></Column>
        <Column
          field="ratioofmovingdurtionts"
          header="Ratio of Moving Durtion (ts)"
        ></Column>
        <Column
          field="ratioofmovingdurtiontm"
          header="Ratio of Moving Durtion (tm)"
        ></Column>
        <Column field="satrtendtimes" header="Satrt End Times"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getMotion from "../../../provider/getMotion";

export default {
  name: "MOResultTable",
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
      if (data == "motion") {
        getMotion((data) => {
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
