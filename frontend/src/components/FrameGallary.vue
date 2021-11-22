<template>
  <ScrollPanel style="width: 100%; height: 360px">
    <div class="col">
        <div v-for="frame in frames">
            <img :src="frame" :key="frame" />
        </div>
    </div>
  </ScrollPanel>
</template>
<script>
let fs = require("fs");
let path = require("path");

export default {
  name: "FrameGallary",
  data() {
    return {
      frames: [],
    };
  },

  created() {
    let frameFolder = path.join(__dirname + "temp/frames")
    
    let files = fs.readdirSync(frameFolder)
    files.sort()
    this.frames = files
      .filter(x => /\.(png|jpg|jpeg|gif)/i.test(x))
      .map(x => path.join(frameFolder, x))
    }
  }
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
