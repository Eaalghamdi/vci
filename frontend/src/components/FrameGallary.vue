<template>
  <ScrollPanel style="width: 100%; height: 360px">
    <div class="col">
      <ul>
        <li>
          <img src="../assets/frames/GA17-Scene-001-01.jpg" />
        </li>
       
      </ul>
    </div>
  </ScrollPanel>
</template>
<script>
export default {
  name: "FrameGallary",
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
