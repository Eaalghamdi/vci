<template>
  <Dialog
    header="Edge Detection"
    v-model:visible="display"
    baseZIndex="999"
    autoZIndex="false"
    position="top"
  >
    <div class="p-field p-col-12">
      <div class="p-formgroup-inline p-col-6">
        <div class="p-field-checkbox">
          <RadioButton
            id="staticSaliency"
            name="staticSaliency"
            value="staticSaliency"
          />
          <label for="city7">Static Sailency</label>
        </div>
        <div class="p-field p-grid">
          <label for="firstname" class="p-col-fixed" style="width:100px">
            Method</label
          >
          <div class="p-col">
            <Dropdown
              v-model="staticSaliencyMethods"
              :options="staticSaliencyMethods"
              optionLabel="name"
              placeholder="Select a Method"
            />
          </div>
        </div>
      </div>

      <div class="p-field p-col-12">
        <div class="p-formgroup-inline ">
          <div class="p-field-checkbox p-col-6">
            <RadioButton
              id="motionSailency"
              name="motionSailency"
              value="motionSailency"
            />
            <label for="city8">Motion Sailency</label>
          </div>
          <div class="p-field p-grid p-col-6">
            <label for="firstname" class="p-col-fixed" style="width:100px">
              Method</label
            >
            <div class="p-col">
              <Dropdown
                v-model="motionSailencyMethods"
                :options="motionSailencyMethods"
                optionLabel="motionSailencyMethods"
                placeholder="Select a Method"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="p-col-3">
      <Button label="Start" class="p-button-sm" />
    </div>
  </Dialog>
</template>
<script>
export default {
  name: "EdgeDetection",
  data() {
    return {
      display: false,
      staticSaliencyMethods: [
        { name: "Spectral Residual", value: 1 },
        { name: "Saliency Fine Grained", value: 2 },
      ],
      motionSailencyMethods: [{ name: "BinWangApr2014", value: 1 }],
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
