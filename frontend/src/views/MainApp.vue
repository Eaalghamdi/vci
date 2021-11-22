<template>
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
</template>

<script>
import VideoPlayer from "@/components/VideoPlayer.vue";
import TopMenu from "@/components/TopMenu.vue";
import Prepreossing from "@/components/Preprocessing.vue";
import FrameExtraction from "@/components/FrameExtraction.vue";
import FrameGallary from "@/components/FrameGallary.vue";

export default {
  name: "MainApp",
  components: {
    VideoPlayer,
    TopMenu,
    FrameExtraction,
    Prepreossing,
    FrameGallary,
  },
};
</script>
<style scoped>
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
  flex-grow: 2;
}

.middleContainer {
}

.videoContainer {
  height: 400px;
}

.p-col {
  margin: 0px;
}
</style>
