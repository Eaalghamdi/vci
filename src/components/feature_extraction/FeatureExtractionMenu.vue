<template>
  <div class="p-fluid p-formgrid p-grid">
    <div class="p-field p-col-12">
      <ul>
        <li>
          <Button
            class="p-button-text"
            label="Object Reecogntion"
            @click="openObjectModal"
          />
        </li>
        <li>
          <Button
            class="p-button-text"
            label="Colorfulness"
            @click="openColorModal"
          />
        </li>
        <li>
          <Button
            class="p-button-text"
            label="Structural Similarity"
            @click="openSSModal"
          />
        </li>
        <li>
          <Button
            class="p-button-text"
            label="Compression"
            @click="openCompressionModel"
          />
        </li>
        <li>
          <Button
            class="p-button-text"
            label="Face Recognition"
            @click="openFaceRecognitionModel"
          />
        </li>
        <li>
          <Button
            class="p-button-text"
            label="Edge Detection"
            @click="openEdgeDetectionModel"
          />
        </li>

        <li>
          <Button
            class="p-button-text"
            label="Motion"
            @click="openMotionModel"
          />
        </li>
        <li>
          <Button
            class="p-button-text"
            label="Sailency"
            @click="openSailencyModel"
          />
        </li>
      </ul>
      <ObjectDetection ref="objectModal" :frmPath="this.framePath" />
      <Colorfulness ref="colorModel" :frmPath="this.framePath" />
      <FrameStructuralSimilarity ref="FSSModel" :frmPath="this.framePath" />
      <Compression ref="CompressionModel" :frmPath="this.framePath" />
      <FaceRecognition ref="FaceRecognitionModel" :frmPath="this.framePath" />
      <Motion ref="MotionModel" :frmPath="this.framePath" />
      <Sailency ref="SailencyModel" :frmPath="this.framePath" />
      <EdgeDetection ref="EdgeDetectionModel" :frmPath="this.framePath" />
    </div>
  </div>
</template>
<script>
import ObjectDetection from "./dialogs/ObjectDetection.vue";
import Colorfulness from "./dialogs/Colorfulness.vue";
import FrameStructuralSimilarity from "./dialogs/FrameStructuralSimilarity.vue";
import Compression from "./dialogs/Compression.vue";
import FaceRecognition from "./dialogs/FaceRecognition.vue";
import Motion from "./dialogs/Motion.vue";
import Sailency from "./dialogs/Sailency.vue";
import EdgeDetection from "./dialogs/EdgeDetection.vue";

export default {
  name: "FeatureExtraction",
  props: ["id", "framePath"],
  components: {
    ObjectDetection,
    Colorfulness,
    FrameStructuralSimilarity,
    Compression,
    FaceRecognition,
    Motion,
    Sailency,
    EdgeDetection,
  },
  data() {},

  methods: {
    openObjectModal() {
      this.$refs.objectModal.showModal();
    },
    openColorModal() {
      this.$refs.colorModel.showModal();
    },
    openSSModal() {
      this.$refs.FSSModel.showModal();
    },
    openCompressionModel() {
      this.$refs.CompressionModel.showModal();
    },
    openFaceRecognitionModel() {
      this.$refs.FaceRecognitionModel.showModal();
    },
    openMotionModel() {
      this.$refs.MotionModel.showModal();
    },
    openSailencyModel() {
      this.$refs.SailencyModel.showModal();
    },
    openEdgeDetectionModel() {
      this.$refs.EdgeDetectionModel.showModal();
    },
  },
};
</script>
<style scoped>
/* .sideMenu {
} */

.p-menu {
  border: none;
}
ul li {
  padding: 5px 0px;
}
ul {
  list-style: none;
  padding-left: 3px;
}
.p-button-text {
  font-size: 1.1rem;
}
.p-button:focus {
  outline: 0 none;
  outline-offset: 0;
  box-shadow: 0 0 0 0px #a7d8a9;
}
.p-button.p-button-text {
  background-color: #81c784;
  color: black;
  border-color: none;
}
</style>
