<template>
  <div>
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>
<script>
export default {
  name: "TopMenu",
  props: ["id"],
  data() {
    return {
      items: [
        { label: "Create Project", icon: "pi pi-folder-open", to: "/" },
        {
          label: "Preprocessing",
          icon: "pi pi-fw pi-video",
          to: "/mainapp/" + this.$route.params.id,
        },
        {
          label: "Feature Extraction",
          icon: "pi pi-fw pi-cog",
          to: "/feauextraction/" + this.$route.params.id,
        }, 
        {
          label: "Visualization",
          icon: "pi pi-chart-line",
          to: "/visualization/" + this.$route.params.id,
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
