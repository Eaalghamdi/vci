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
        <Column field="imgname" header="Iamge Name"></Column>
        <Column field="classindex" header="Class Index"></Column>
        <Column field="confidence" header="Confidence"></Column>
        <Column field="bbox" header="BBox"></Column>
      </DataTable>
    </ScrollPanel>
  </div>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../../utils/config";
import getObjectDetection from "../../../provider/getObjectDetection";

export default {
  name: "ODResultTable",
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
      if (data == "objectdetection") {
        getObjectDetection((data) => {
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
