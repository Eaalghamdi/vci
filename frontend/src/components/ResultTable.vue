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
        { Shot: 0, KeyFrame: 1, img_szieByte: 57411, img_szieKB: 57.411 },
        { Shot: 0, KeyFrame: 0, img_szieByte: 56321, img_szieKB: 56.321 },
        { Shot: 1, KeyFrame: 3, img_szieByte: 28805, img_szieKB: 28.805 },
        { Shot: 2, KeyFrame: 6, img_szieByte: 31207, img_szieKB: 31.207 },
        { Shot: 2, KeyFrame: 4, img_szieByte: 39170, img_szieKB: 39.17 },
        { Shot: 2, KeyFrame: 5, img_szieByte: 6800, img_szieKB: 6.8 },
        { Shot: 3, KeyFrame: 7, img_szieByte: 22031, img_szieKB: 22.031 },
        { Shot: 4, KeyFrame: 8, img_szieByte: 17918, img_szieKB: 17.918 },
        { Shot: 4, KeyFrame: 9, img_szieByte: 30246, img_szieKB: 30.246 },
        { Shot: 5, KeyFrame: 10, img_szieByte: 23830, img_szieKB: 23.83 },
        { Shot: 5, KeyFrame: 11, img_szieByte: 21317, img_szieKB: 21.317 },
        { Shot: 6, KeyFrame: 12, img_szieByte: 17008, img_szieKB: 17.008 },
        { Shot: 7, KeyFrame: 13, img_szieByte: 26718, img_szieKB: 26.718 },
        { Shot: 7, KeyFrame: 14, img_szieByte: 30583, img_szieKB: 30.583 },
        { Shot: 8, KeyFrame: 16, img_szieByte: 37113, img_szieKB: 37.113 },
        { Shot: 8, KeyFrame: 15, img_szieByte: 31465, img_szieKB: 31.465 },
        { Shot: 9, KeyFrame: 17, img_szieByte: 72280, img_szieKB: 72.28 },
        { Shot: 9, KeyFrame: 18, img_szieByte: 74018, img_szieKB: 74.018 },
        { Shot: 10, KeyFrame: 19, img_szieByte: 26904, img_szieKB: 26.904 },
        { Shot: 10, KeyFrame: 20, img_szieByte: 33935, img_szieKB: 33.935 },
        { Shot: 11, KeyFrame: 22, img_szieByte: 16506, img_szieKB: 16.506 },
        { Shot: 11, KeyFrame: 21, img_szieByte: 25111, img_szieKB: 25.111 },
        { Shot: 12, KeyFrame: 24, img_szieByte: 70419, img_szieKB: 70.419 },
        { Shot: 12, KeyFrame: 23, img_szieByte: 22331, img_szieKB: 22.331 },
        { Shot: 13, KeyFrame: 25, img_szieByte: 8955, img_szieKB: 8.955 },
        { Shot: 14, KeyFrame: 26, img_szieByte: 38658, img_szieKB: 38.658 },
        { Shot: 15, KeyFrame: 27, img_szieByte: 16742, img_szieKB: 16.742 },
        { Shot: 15, KeyFrame: 28, img_szieByte: 31517, img_szieKB: 31.517 },
        { Shot: 16, KeyFrame: 30, img_szieByte: 59811, img_szieKB: 59.811 },
        { Shot: 16, KeyFrame: 29, img_szieByte: 50791, img_szieKB: 50.791 },
        { Shot: 17, KeyFrame: 31, img_szieByte: 41845, img_szieKB: 41.845 },
        { Shot: 17, KeyFrame: 33, img_szieByte: 36797, img_szieKB: 36.797 },
        { Shot: 17, KeyFrame: 32, img_szieByte: 41543, img_szieKB: 41.543 },
        { Shot: 18, KeyFrame: 34, img_szieByte: 18914, img_szieKB: 18.914 },
        { Shot: 19, KeyFrame: 35, img_szieByte: 57665, img_szieKB: 57.665 },
        { Shot: 20, KeyFrame: 37, img_szieByte: 53241, img_szieKB: 53.241 },
        { Shot: 20, KeyFrame: 36, img_szieByte: 68089, img_szieKB: 68.089 },
        { Shot: 21, KeyFrame: 39, img_szieByte: 65031, img_szieKB: 65.031 },
        { Shot: 21, KeyFrame: 38, img_szieByte: 53628, img_szieKB: 53.628 },
        { Shot: 21, KeyFrame: 40, img_szieByte: 82357, img_szieKB: 82.357 },
        { Shot: 22, KeyFrame: 43, img_szieByte: 60005, img_szieKB: 60.005 },
        { Shot: 22, KeyFrame: 42, img_szieByte: 78247, img_szieKB: 78.247 },
        { Shot: 22, KeyFrame: 41, img_szieByte: 81080, img_szieKB: 81.08 },
        { Shot: 23, KeyFrame: 44, img_szieByte: 47906, img_szieKB: 47.906 },
        { Shot: 23, KeyFrame: 45, img_szieByte: 36671, img_szieKB: 36.671 },
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
