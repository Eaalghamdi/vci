<template>
  <div>
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>
<script>
export default {
  name: "TopMenu",
  props: ["id", "filePath", "fileName"],
  data() {
    return {
      items: [
        { label: "Create Project", icon: "pi pi-folder-open", to: "/" },
        {
          label: "Preprocessing",
          icon: "pi pi-fw pi-video",
          to:
            "/mainApp/" +
            this.$route.params.id +
            "/" +
            this.$route.params.filePath.split('/').join(',') +
            "/" +
            this.$route.params.fileName,
        },
        {
          label: "Feature Extraction",
          icon: "pi pi-fw pi-cog",
          to:
            "/feauextraction/" +
            this.$route.params.id +
            "/" +
            this.$route.params.filePath.split('/').join(',') +
            "/" +
            this.$route.params.fileName,
        },
        {
          label: "Visualization",
          icon: "pi pi-chart-line",
          to:
            "/visualization/" +
            this.$route.params.id +
            "/" +
            this.$route.params.filePath.split('/').join(',') +
            "/" +
            this.$route.params.fileName,
        },
      ],
    };
  },
};
</script>
<style scoped>
.p-tabmenu {
  background: #1e1e1e;
}
</style>
