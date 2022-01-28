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
            <FrameExtraction />
          </div>
          <div class="p-col row-down">
            <Prepreossing />
          </div>
        </div>
      </div>
      <div class="p-col col-2">
        <div class="middleContainer">
          <div class="p-col row-top">
            <div class="videoContainer">
              <VideoPlayer />
            </div>
          </div>
          <div class="p-col row-down">
            <FrameGallary />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VideoPlayer from "../components/main_app/VideoPlayer.vue";
import TopMenu from "../components/TopMenu.vue";
import Prepreossing from "../components/main_app/Preprocessing.vue";
import FrameExtraction from "../components/main_app/FrameExtraction.vue";
import FrameGallary from "../components/main_app/FrameGallary.vue";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../utils/config";

export default {
  name: "MainApp",
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
    VideoPlayer,
    TopMenu,
    FrameExtraction,
    Prepreossing,
    FrameGallary,
  },

  mounted() {
    ipcRenderer.on(ipcKeys.mainAppLoadingAck, (event, data) => {
      if (data == "loadnow") {
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
.cont {
  display: flex;
  height: 100%;
  padding-top: 18px;
  max-height: 100%;
  padding-bottom: 15px;
  padding-left: 15px;
  padding-right: 15px;
}

.SideMenu {
  height: 100vh;
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
  flex-grow: 2;
}

.videoContainer {
  height: 400px;
}

.p-col {
  margin: 0px;
}
</style>
