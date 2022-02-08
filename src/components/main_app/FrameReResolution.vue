<template>
  <Panel>
    <div class="p-fluid p-grid">
      <div class="p-field p-col-12">
        <p>Image Resolution Converter</p>
        <div class="p-field p-grid">
          <label for="Height" class="p-col-fixed" style="width: 100px"
            >Height</label
          >
          <div class="p-col">
            <InputText id="Height" type="text" />
          </div>
        </div>
        <div class="p-field p-grid">
          <label for="Width" class="p-col-fixed" style="width: 100px"
            >Width</label
          >
          <div class="p-col">
            <InputText id="Width" type="text" />
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
  name: "FrameReResolution",
  data() {
    return {
      Compression: null,
    };
  },
};
</script>
<style scoped>
.p-col {
  padding-top: 15px;
  padding-bottom: 15px;
}
.p-field-checkbox {
  padding-bottom: 15px;
}
.p-col-3 {
  padding-top: 15px;
}

.p-slider-horizontal,
.p-inputtext {
  width: 18rem;
}
</style>
