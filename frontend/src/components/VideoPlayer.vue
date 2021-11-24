<template>
  <video
    id="player"
    key="VideoPath"
    playsinline
    controls
    data-poster="/path/to/poster.jpg"
  >
    <source src="../assets/1.mp4" type="video/mp4" />
  </video>
</template>
<script>
import axios from "axios";

export default {
  name: "VideoPlayer",
  props: ["id"],
  data() {
    return {
      VideoPath: " ",
    };
  },
  methods: {
    getVideoURL() {
      axios
        .get("http://127.0.0.1:8000/api/projects/" + this.$route.params.id)
        .then((response) => {
          this.VideoPath = response.data.VideoPath;

          console.log("from Video Player: " + this.$route.params.id);
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
