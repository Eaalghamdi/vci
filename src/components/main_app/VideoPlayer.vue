<template>
  <video id="player" :key="VideoPath" playsinline controls>
    <source :src="videoSrc" type="video/mp4" />
  </video>
</template>
<script>
// import { ipcRenderer } from "electron";
import { ipcKeys, eventKeys } from "../../utils/config";
import event from "../../utils/event";

export default {
  name: "VideoPlayer",
  props: ["id", "filePath", "fileName"],

  data() {
    return {
      VideoPath: "",
      videoSrc: "",
    };
  },

  mounted() {
    event.on(eventKeys.getProjectData, (data) => {
      this.videoSrc = "video-server://" + data["VideoTitle"];
    });
  },
};
</script>
<style scoped>
#player {
  height: inherit;
  width: 100%;
}
</style>
