<template>
  <div>
    <TabView>
      <TabPanel v-for="tab in tabs" :key="tab.title" :header="tab.title">
        <p>{{ tab.content }}</p>
      </TabPanel>
    </TabView>
  </div>
</template>
<script>
export default {
  name: "BottomTabs",
  data() {
    return {
      tabs: [
        { title: "Prepreossing", content: "Content 1" },
        { title: "Feature Extraxtion", content: "Content 2" },
        { title: "Help", content: "Content 3" },
      ],
    };
  },
};
</script>
<style lang=""></style>
