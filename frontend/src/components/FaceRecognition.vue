<template>
  <div>
    <Dialog
      header="Face Recognition & Tracking"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="top"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <div class="p-field p-grid">
            <label for="method" class="p-col-fixed" style="width:100px">
              Method</label
            >
            <div class="p-col">
              <Dropdown
                v-model="selectedCity1"
                :options="cities"
                optionLabel="name"
                placeholder="Select a Method"
              />
            </div>
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
  name: "FaceRecognition",
  data() {
    return {
      display: false,
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
