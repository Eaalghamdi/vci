<template>
  <ScrollPanel style="width: 100%; height: 360px">
    <div class="col">
      <ul>
        <li v-for="image in images">
          <img
            :src="'data:image/jpg;base64,' + image.base64"
            :key="image"
          />
        </li>
      </ul>
    </div>
  </ScrollPanel>
</template>
<script>
import fs from "fs";
import path from "path";

export default {
  name: "FrameGallary",
  data() {
    return {
      images: [],
      sourcePath: null,
    };
  },

  methods: {
    scan() {
      // Iterate over all files in directory
      const outFrames =
        "../assets/temp/frames";
      let files = fs.readdirSync(outFrames);
      const regex = /.jpe?g$/gim;
      for (let file of files) {
        // Ignore non jpg files
        if (!file.match(regex)) {
          continue;
        }
        let image = {};
        image.name = file;
        image.path = path.join(outFrames, file);
        console.log(image);
        image.base64 = new Buffer(fs.readFileSync(image.path)).toString(
          "base64"
        );
        this.images.push(image);
      }
    },
  },
  created() {
    this.scan();
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
