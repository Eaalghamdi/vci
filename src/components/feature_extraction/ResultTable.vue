<template>
  <div>
    <DataTable
      :value="products"
      :scrollable="true"
      scrollHeight="400px"
      :loading="loading"
      class="p-datatable-sm"
    >
      <template #header>
        <div style="text-align: right">
          <Button
            icon="pi pi-external-link"
            label="Export"
            @click="exportCSV($event)"
          />
        </div>
      </template>
      <Column field="Shot" header="shot"></Column>
      <Column field="KeyFrame" header="Keyframe"></Column>
      <Column field="img_szieByte" header="Frame File Szie (byte)"></Column>
      <Column field="img_szieKB" header="	Frame File Szie (Kilobyte)"></Column>
    </DataTable>
  </div>
</template>
<script>
export default {
  name: "ResultTable",
  data() {
    return {
      products: [
        { Shot: 0, KeyFrame: 2, img_szieByte: 38576, img_szieKB: 38.576 },
        { Shot: 1, KeyFrame: 1, img_szieByte: 57411, img_szieKB: 57.411 },
        { Shot: 2, KeyFrame: 0, img_szieByte: 56321, img_szieKB: 56.321 },

      ],
    };
  },
  methods: {
    exportCSV() {
      this.$refs.dt.exportCSV();
    },
  },
};
</script>
<style scoped>
.logo {
  color: #e78200;
}
</style>
