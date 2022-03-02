<template>
  <ScrollPanel style="height: 320px">
    <div class="col">
      <ul>
        <li v-for="image in images" v-bind:key="image.id">
          <img :src="'data:image/jpg;base64,' + image.base64" :key="image" />
        </li>
      </ul>
    </div>
    <p>{{ VideoPath }}</p>
  </ScrollPanel>
</template>
<script>
import getGallary from "../../provider/getGallary";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../utils/config";

export default {
  name: "FrameGallary",
  props: ["id", "filePath", "fileName"],

  data() {
    return {
      images: [],
      sourcePath: null,
      VideoPath:
        (this.$route.params.filePath.includes(",")
          ? this.$route.params.filePath.split(',').join('/')
          : this.$route.params.filePath) +
        "/" +
        this.$route.params.fileName,
    };
  },

  mounted() {
    getGallary(
      (image) => {
        this.images.push(image);
      },
      this.$route.params.filePath.includes(",")
        ? this.$route.params.filePath.split(',').join('/')
        : this.$route.params.filePath,
      this.$route.params.fileName
    );
    ipcRenderer.on(ipcKeys.getGallaryAck, (event, data) => {
      this.images = [];
      getGallary(
        (image) => {
          this.images.push(image);
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopload");
        },
        this.$route.params.filePath.includes(",")
          ? this.$route.params.filePath.split(',').join('/')
          : this.$route.params.filePath,
        this.$route.params.fileName
      );
    });
  },
};
</script>
<style scoped>
ul {
  text-align: left;
  padding: 0;
}

li {
  width: auto;
  display: inline-block;
  vertical-align: top;
  padding: 2px;
}

li img {
  width: 145px;
  max-width: 145px;
  height: 90px;
}
</style>
