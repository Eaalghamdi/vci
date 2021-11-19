<template>
  <div>
    <Dialog
      header="Colorfulness"
      v-model:visible="display"
      baseZIndex="999"
      autoZIndex="false"
      position="center"
    >
      <div class="p-fluid p-formgrid p-grid">
        <div class="p-field p-col-12">
          <div class="p-formgroup-inline">
            <div class="p-field-checkbox">
              <Checkbox
                id="Single"
                name="Single"
                value="Single"
                v-model="single"
              />
              <label for="Single">Single</label>
            </div>
            <div class="p-field-checkbox">
              <Checkbox id="Pairs" name="Pairs" value="Pairs" v-model="pairs" />
              <label for="Pairs"> Pairs</label>
            </div>
          </div>
          <div class="p-field p-grid">
            <label for="firstname" class="p-col-fixed" style="width:100px">
              Method</label
            >
            <div class="p-col">
              <Dropdown
                v-model="colorfulness"
                :options="colorfulness"
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
  name: "Colorfulness",
  data() {
    return {
      display: false,
      single: "1",
      pairs: "2",
      colorfulness: [
        {
          name: "Hasler and Süsstrunk",
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
Hasler and Süsstrunk
