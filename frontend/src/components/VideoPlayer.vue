<template>
  <video
    id="player"
    :key="f"
    playsinline
    controls
    data-poster="/path/to/poster.jpg"
  >
    <source src="../assets/GA17.mp4" type="video/mp4" />
  </video>
</template>
<script>
import axios from "axios";

export default {
  name: "VideoPlayer",
  props: ["id"],
  data() {
    return {
      videoFile: "",
      f: "https://www.youtube.com/watch?v=jt9LlHXGckg",
    };
  },
  methods: {
    getVideoURL() {
      axios
        .get("http://127.0.0.1:8000/api/projects/" + this.$route.params.id)
        .then((response) => {
          this.videoFile = "../assets/" + response.data;
          console.log(this.videoFile);
        })
        .catch(function(error) {
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
