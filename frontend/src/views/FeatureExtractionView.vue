<template>
  <TopMenu />
  <div class="p-grid cont ">
    <div class="SideMenu">
      <div class="p-col col-1">
        <div class="p-col row-top">
          <FeatureExtractionMenu />
        </div>
        <div class="p-col row-down">
          <ResultsMenu />
        </div>
      </div>
    </div>
    <div class="p-col col-2">
      <div class="middleContainer">
        <div class="p-col row-top">
          <div class="Results">
            <ResultTable />
          </div>
        </div>
        <div class="p-col row-down"></div>
      </div>
    </div>
  </div>
  <Bottom />
</template>
<script>
import TopMenu from "@/components/TopMenu.vue";
import FeatureExtractionMenu from "@/components/FeatureExtractionMenu.vue";
import ResultsMenu from "@/components/ResultsMenu.vue";
import ResultTable from "@/components/ResultTable.vue";

export default {
  name: "FeatureExtractionView",
  props: ["id"],
  components: {
    TopMenu,
    FeatureExtractionMenu,
    ResultsMenu,
    ResultTable,
  },
};
</script>
<style scoped>
.SideMenu {
  margin: 0px;
  background-color: #1e1e1e;
}
.cont {
  display: felx;
  padding-top: 18px;
  padding-bottom: 0px;
  padding-left: 15px;
  padding-right: 15px;
}

.SideMenu {
  margin: 0px;
  background-color: #1e1e1e;
}

.row-top {
  margin: 0px;
}
.row-down {
  margin: 0px;
}

.col-1 {
  width: 400px;
  min-width: 400px;
}

.col-2 {
  flex-grow: 3;
}

.middleContainer {
}

.p-col {
  margin: 0px;
}
</style>
