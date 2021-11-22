<template>
  <div>
    <Dialog
      header="Motion"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="top"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <label for="method" class="p-col-fixed" style="width: 100px">
            Method</label
          >
          <div class="p-col">
            <Dropdown
              v-model="motionMethods"
              :options="motionMethods"
              optionLabel="motionMethods"
              placeholder="Select a Method"
            />
          </div>
          <div class="p-field p-col-12">
            <label for="stacked">Kernal Size</label>
            <InputNumber id="Kernal" v-model="motionKernalSize" showButtons />
          </div>
          <div class="p-field p-col-12">
            <label for="stacked">Countor Size</label>
            <InputNumber id="Countor" v-model="motionCountorSize" showButtons />
          </div>
        </div>

        <div class="p-col-3">
          <Button label="Start" class="p-button-sm" />
        </div>
      </div>
    </Dialog>
  </div>
</template>
<script>
export default {
  name: "Motion",
  data() {
    return {
      display: false,
      motionMethods: [{ name: "Alghamdi", value: 1 }],
    };
  },
  methods: {
    showModal() {
      this.display = true;
    },
  },
};
</script>
<style></style>
