<template>
  <div>
    <Dialog
      header="Frame Structural Similarity"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="top"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <div class="p-formgroup-inline">
            <div class="p-field-checkbox">
              <Checkbox
                id="ssiSingle"
                name="ssiSingle"
                value="ssiSingle"
                v-model="single"
              />
              <label for="Single">Single</label>
            </div>
            <div class="p-field-checkbox">
              <Checkbox
                id="ssiPairs"
                name="ssiPairs"
                value="ssiPairs"
                v-model="ssiPairs"
              />
              <label for="ssiPairs"> Pairs</label>
            </div>
          </div>
          <div class="p-field p-grid">
            <label for="firstname" class="p-col-fixed" style="width: 100px">
              Method</label
            >
            <div class="p-col">
              <Dropdown
                v-model="SSI"
                :options="SSI"
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
  name: "FrameStructuralSimilarity",
  data() {
    return {
      display: false,
      SSI: [
        {
          name: "SSIM",
          value: 1,
        },
      ],
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
