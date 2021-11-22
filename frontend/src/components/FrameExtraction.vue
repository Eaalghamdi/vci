<template>
  <Panel header="Frame Extraction">
    <div class="p-fluid p-formgrid p-grid">
      <div class="p-field p-col-12">
        <h4>Shot Bundry Detection</h4>
        <div class="p-field p-grid">
          <label for="method" class="p-col-fixed" style="width: 100px">
            Method</label
          >
          <div class="p-col">
            <Dropdown
              v-model="shotDetectors"
              :options="shotDetectors"
              optionLabel="name"
              placeholder="Select a detector"
            />
          </div>
        </div>
        <div class="p-field p-grid">
          <label for="lastname" class="p-col-fixed" style="width: 100px"
            >Treshold</label
          >
          <div class="p-col">
            <InputNumber
              id="horizontal"
              v-model="value18"
              showButtons
              buttonLayout="horizontal"
              :step="1"
              decrementButtonClass="p-button-danger"
              incrementButtonClass="p-button-success"
              incrementButtonIcon="pi pi-plus"
              decrementButtonIcon="pi pi-minus"
            />
          </div>
        </div>

        <div class="p-field p-col-12">
          <h4>Manual Frame</h4>
        </div>
        <div class="p-field p-grid">
          <label for="lastname" class="p-col-fixed" style="width: 100px">
            Per Second</label
          >
          <div class="p-col">
            <InputNumber
              id="horizontal"
              v-model="value18"
              showButtons
              buttonLayout="horizontal"
              :step="1"
              decrementButtonClass="p-button-danger"
              incrementButtonClass="p-button-success"
              incrementButtonIcon="pi pi-plus"
              decrementButtonIcon="pi pi-minus"
            />
          </div>
        </div>
      </div>
      <div class="p-col-3">
        <Button label="Start" class="p-button-sm" />
      </div>
    </div>
  </Panel>
</template>
<script>
export default {
  name: "FrameExtraction",
  data() {
    return {
      shotDetectors: [
        {
          name: "Content Detector",
          value: 1,
        },
        { name: "Threshold Detector", value: 2 },
      ],
    };
  },
};
</script>
<style scoped>
.p-slider-horizontal,
.p-inputtext {
  width: 18rem;
}
</style>
