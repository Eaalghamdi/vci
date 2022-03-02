<template>
  <video id="player" :key="VideoPath" playsinline controls>
    <source :src="videoSrc" type="video/mp4" />
  </video>
</template>
<script>
// import { ipcRenderer } from "electron";
// import { ipcKeys, eventKeys } from "../../utils/config";

export default {
  name: "VideoPlayer",

  data() {
    return {
      VideoPath: "",
      videoSrc: "video-server://" + this.$route.params.fileName,
    };
  },

};
</script>
<style scoped>
#player {
  height: inherit;
  width: 100%;
}
</style>
