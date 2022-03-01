<template>
  <Panel header="Results">
    <div class="p-fluid p-formgrid p-grid">
      <div class="p-field p-col-12">
        <ul>
          <li>
            <Button
              @click="onOR"
              label="Object Reecognition"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onCF"
              label="Colorfulness"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onSS"
              label="Structural Similarity"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onCO"
              label="Compression"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onFR"
              label="Face Recognition"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onED"
              label="Edge Detectin"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onMO"
              label="Motion"
              class="p-button-text p-button-plain"
            />
          </li>
          <li>
            <Button
              @click="onSA"
              label="Sailency"
              class="p-button-text p-button-plain"
            />
          </li>
        </ul>
      </div>
    </div>
  </Panel>
</template>
<script>
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../utils/config";

export default {
  name: "ResultsMenu",
  methods: {
    onOR() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "odresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "objectdetection");
    },
    onCF() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "cfresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "colorfulness");
    },
    onSS() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "ssresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "structsimilarity");
    },
    onCO() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "coresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "compression");
    },
    onFR() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "fdresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "facedetection");
    },
    onED() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "edresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "edgedetection");
    },
    onMO() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "moresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "motion");
    },
    onSA() {
      ipcRenderer.send(ipcKeys.mainAppLoading, "loadfe");
      ipcRenderer.send(ipcKeys.panelVisibility, "saresultshow");
      ipcRenderer.send(ipcKeys.getResultTable, "saliency");
    },
  },
};
</script>
<style scoped>
</style>
