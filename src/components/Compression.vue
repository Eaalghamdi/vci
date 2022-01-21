<template>
  <div>
    <Dialog
      header="Compression"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="top"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <div class="p-formgroup-inline">
            <div class="p-field-checkbox">
              <Checkbox id="MPEG" name="MPEG" value="MPEG" v-model="cities2" />
              <label for="MPEG">MPEG</label>
            </div>
            <div class="p-field-checkbox">
              <Checkbox id="H264" name="H264" value="H264" v-model="cities2" />
              <label for="H264"> H264</label>
            </div>
            <div class="p-field-checkbox">
              <Checkbox id="H265" name="H265" value="H265" v-model="cities2" />
              <label for="H265"> H265</label>
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
  name: "Compression",
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
