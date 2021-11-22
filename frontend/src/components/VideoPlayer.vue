<template>
  <video
    id="player"
    :key="videoFile"
    playsinline
    controls
    data-poster="/path/to/poster.jpg"
  >
    <source src="" type="video/mp4" />
  </video>
</template>
<script>
import axios from "axios";

export default {
  name: "VideoPlayer",
  props: ["id"],
  data() {
    return {
      videoFile: " ",
    };
  },
  methods: {
    getVideoURL() {
      axios
        .get("http://127.0.0.1:8000/api/projects/" + this.$route.params.id)
        .then((response) => {
          this.videoFile = response.data.VideoPath;

          console.log("from Video Player: " + this.videoFile);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },

  created() {
    this.getVideoURL();
  },
};
</script>
<style scoped>
#player {
  height: inherit;
  width: 100%;
}
</style>
