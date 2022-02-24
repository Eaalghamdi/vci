<template>
  <div>
    <loading
      v-model:active="isLoading"
      :can-cancel="false"
      :is-full-page="fullPage"
      :color="color"
      :background-color="bgColor"
      :loader="loaderDesgin"
      :opacity="opacity"
    />

    <TopMenu />
    <div class="p-grid cont">
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
  </div>
</template>
<script>
import TopMenu from "../components/common/TopMenu.vue";
import FeatureExtractionMenu from "../components/feature_extraction/FeatureExtractionMenu.vue";
import ResultsMenu from "../components/feature_extraction/ResultsMenu.vue";
import ResultTable from "../components/feature_extraction/ResultTable.vue";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../utils/config";

export default {
  name: "FeatureExtraction",
  props: ["id"],
  data() {
    return {
      isLoading: false,
      fullPage: true,
      color: "#ff8c00",
      bgColor: "#1a1a1a",
      loaderDesgin: "dots",
      opacity: 0.85,
    };
  },
  components: {
    Loading,
    TopMenu,
    FeatureExtractionMenu,
    ResultsMenu,
    ResultTable,
  },
  mounted() {
    ipcRenderer.on(ipcKeys.mainAppLoadingAck, (event, data) => {
      if (data == "loadfe") {
        this.isLoading = true;
      } else {
        this.isLoading = false;
      }
      ipcRenderer.removeListener(ipcKeys.mainAppLoadingAck, () => {});
    });
  },
};
</script>
<style scoped>
.SideMenu {
  margin: 0px;
  background-color: #1e1e1e;
}
.cont {
  display: flex;
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

/* .middleContainer {
} */

.p-col {
  margin: 0px;
}
</style>
