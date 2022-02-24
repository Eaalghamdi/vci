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
            <FeatureExtractionMenu :framePath="framePathData" />
          </div>
          <div class="p-col row-down">
            <ResultsMenu />
          </div>
        </div>
      </div>
      <div class="p-col col-2">
        <div class="middleContainer">
          <div class="p-col row-top">
            <div v-if="!isCFResultHidden" class="Results">
              <CFResultTable />
            </div>
            <div v-if="!isEDResultHidden" class="Results">
              <EDResultTable />
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
import CFResultTable from "../components/feature_extraction/result_table/CFResultTable.vue";
import EDResultTable from "../components/feature_extraction/result_table/EDResultTable.vue";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
import getProject from "../provider/getProject";
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
      isCFResultHidden: true,
      isEDResultHidden: true,
    };
  },
  components: {
    Loading,
    TopMenu,
    FeatureExtractionMenu,
    ResultsMenu,
    CFResultTable,
    EDResultTable,
  },
  mounted() {
    this.isLoading = true;

    setTimeout(() => {
      getProject((data) => {
        this.framePathData = data;
        ipcRenderer.send(ipcKeys.mainAppLoading, "stoploadfe");
      }, this.$route.params.id);
    }, 1000);

    ipcRenderer.on(ipcKeys.panelVisibilityAck, (event, data) => {
      if (data == "cfresultshow") {
        this.isCFResultHidden = false;
      } else {
        this.isCFResultHidden = true;
      }
      if (data == "edresultshow") {
        this.isEDResultHidden = false;
      } else {
        this.isEDResultHidden = true;
      }
      ipcRenderer.removeListener(ipcKeys.panelVisibilityAck, () => {});
    });

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

.p-col {
  margin: 0px;
}
</style>
