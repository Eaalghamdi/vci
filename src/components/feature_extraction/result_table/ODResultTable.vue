<template>
  <div>
    <div style="text-align: right">
      <Button icon="pi pi-external-link" label="Export" @click="exportCSV()" />
    </div>
    <ScrollPanel style="height: 600px" class="custom">
      <DataTable :value="products" style="width: 1000px">
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
import toExcel from "../../../provider/toExcel";

export default {
  name: "ODResultTable",
  data() {
    return {
      products: [],
      exportData: [
        {
          id: 1,
          test: "eatew",
          rest: "asasas",
        },
        {
          id: 2,
          test: "eatew",
          rest: "asasas",
        },
      ],
    };
  },
  methods: {
    exportCSV() {
      toExcel(this.products, "objectrecognition");
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
