<template>
  <video id="player" :key="VideoPath" playsinline controls>
    <source
      src="video-server://file_example_MP4_640_3MG.mp4"
      type="video/mp4"
    />
  </video>
</template>
<script>
// import axios from "axios";
// const path = require("path");

export default {
  name: "VideoPlayer",
  props: ["id"],
  data() {
    return {
      VideoPath: "",
    };
  },

  created() {
    //
    // let videoid = "http://127.0.0.1:8000/api/projects/" + this.$route.params.id
    // axios
    //   .get(videoid)
    //   .then((response) => {
    //     this.VideoPath = response.data.VideoPath;
    //     console.log( this.VideoPath)
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   });
  },
};
</script>
<style scoped>
#player {
  height: inherit;
  width: 100%;
}
</style>
