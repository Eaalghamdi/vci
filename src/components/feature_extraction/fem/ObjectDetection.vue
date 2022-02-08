<template>
  <div>
    <Dialog
      header="Object Detection"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="top"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <div class="p-formgroup-inline">
            <div class="p-field-checkbox">
              <RadioButton
                id="city7"
                name="city2"
                value="Chicago"
                v-model="city2"
              />
              <label for="city7">Chicago</label>
            </div>
            <div class="p-field-checkbox">
              <RadioButton
                id="city8"
                name="city2"
                value="Los Angeles"
                v-model="city2"
              />
              <label for="city8">Los Angeles</label>
            </div>
          </div>
          <div class="p-field p-grid">
            <label for="firstname" class="p-col-fixed" style="width: 100px">
              Method</label
            >
            <div class="p-col">
              <Dropdown
                v-model="selectedCity1"
                :options="cities"
                optionLabel="name"
                placeholder="Select a City"
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
  name: "ObjectDetection",
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
