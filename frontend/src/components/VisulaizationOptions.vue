<template>
  <Panel header="Plot Results">
    <div class="p-fluid p-formgrid p-grid">
      <div class="p-field p-col-12">
        <div class="p-field p-grid">
          <label for="method" class="p-col-fixed" style="width:100px"> </label>
          <div class="p-col">
            <Dropdown
              v-model="selectedCity1"
              :options="cities"
              optionLabel="name"
              placeholder="Select an analysis"
            />
          </div>
        </div>
      </div>
      <div class="p-field p-col-12">
        <div class="p-field p-grid">
          <label for="method" class="p-col-fixed" style="width:100px">
            Y
          </label>
          <div class="p-col">
            <Dropdown
              v-model="selectedCity1"
              :options="cities"
              optionLabel="name"
              placeholder="Select data"
            />
          </div>
        </div>
      </div>
      <div class="p-field p-col-12">
        <div class="p-field p-grid">
          <label for="method" class="p-col-fixed" style="width:100px">
            X
          </label>
          <div class="p-col">
            <Dropdown
              v-model="selectedCity1"
              :options="cities"
              optionLabel="name"
              placeholder="Select data"
            />
          </div>
        </div>
      </div>
      <div class="p-col-4">
        <Button label="Create" type="submit" />
      </div>
    </div>
  </Panel>
</template>
<script>
export default {
  name: "VisulaizationOptions",
  data() {
    return {
      selectedCity: null,
      cities: [
        { name: "Object Recognition Results", code: "NY" },
        { name: "Colofulness Results", code: "RM" },
        { name: "Compression Results", code: "LDN" },
        { name: "Motion Results", code: "IST" },
        { name: "Edge Results", code: "PRS" },
      ],
    };
  },
};
</script>
<style scoped>
.center {
  text-align: center;
}
</style>
