<template>
  <Panel header="Frame Extraction">
    <div class="p-fluid p-grid">
      <div class="p-field p-col-12">
        <div>
          <div class="p-field-checkbox-a">
            <RadioButton
              id="shot-boundry-detection"
              name="Shot Bundry Detection"
              value="1"
              v-model="slectedFrameExtrac"
            />
            <label class="radio-label" for="shot-boundry-detection"
              >Shot Bundry Detection</label
            >
          </div>
          <div class="p-field-checkbox-b">
            <RadioButton
              id="manual-frame"
              name="Manual Frame"
              value="2"
              v-model="slectedFrameExtrac"
            />
            <label class="radio-label" for="manual-frame">Manual Frame</label>
          </div>
        </div>
        <div v-if="slectedFrameExtrac == 1" class="fe-panel">
          <div class="p-field p-grid">
            <Panel class="img-res">
              <div class="p-field p-col-12">
                <p>Image Resolution Converter (Optional)</p>
                <div class="p-field p-grid">
                  <label for="Height" class="p-col-fixed" style="width: 100px"
                    >Height</label
                  >
                  <div class="p-col">
                    <InputText id="Height" type="text" v-model="newHeight" />
                  </div>
                </div>
                <div class="p-field p-grid">
                  <label for="Width" class="p-col-fixed" style="width: 100px"
                    >Width</label
                  >
                  <div class="p-col">
                    <InputText id="Width" type="text" v-model="newWidth" />
                  </div>
                </div>
              </div>
            </Panel>
            <label for="method" class="p-col-fixed" style="width: 100px">
              Method</label
            >
            <div class="p-col">
              <Dropdown
                v-model="selectedMethod"
                :options="methodList"
                optionLabel="name"
                optionValue="value"
                placeholder="Select a detector"
              />
            </div>
          </div>
          <div class="p-field p-grid">
            <label for="lastname" class="p-col-fixed" style="width: 100px"
              >Treshold</label
            >
            <div class="p-col">
              <InputNumber
                id="horizontal"
                v-model="thrValue"
                showButtons
                buttonLayout="horizontal"
                :step="1"
                decrementButtonClass="p-button-danger"
                incrementButtonClass="p-button-success"
                incrementButtonIcon="pi pi-plus"
                decrementButtonIcon="pi pi-minus"
              />
            </div>
          </div>
        </div>
        <div v-if="slectedFrameExtrac == 2" class="fe-panel">
          <div class="p-field p-grid">
            <Panel class="img-res">
              <div class="p-field p-col-12">
                <p>Image Resolution Converter (Optional)</p>
                <div class="p-field p-grid">
                  <label for="Height" class="p-col-fixed" style="width: 100px"
                    >Height</label
                  >
                  <div class="p-col">
                    <InputText id="Height" type="text" v-model="newHeight" />
                  </div>
                </div>
                <div class="p-field p-grid">
                  <label for="Width" class="p-col-fixed" style="width: 100px"
                    >Width</label
                  >
                  <div class="p-col">
                    <InputText id="Width" type="text" v-model="newWidth" />
                  </div>
                </div>
              </div>
            </Panel>
            <label for="lastname" class="p-col-fixed" style="width: 100px">
              Per Second</label
            >
            <div class="p-col">
              <InputNumber
                id="horizontal"
                v-model="secValue"
                showButtons
                buttonLayout="horizontal"
                :step="1"
                decrementButtonClass="p-button-danger"
                incrementButtonClass="p-button-success"
                incrementButtonIcon="pi pi-plus"
                decrementButtonIcon="pi pi-minus"
              />
            </div>
          </div>
        </div>
      </div>
      <div v-if="slectedFrameExtrac != null" class="p-col-3">
        <Button @click="onFrameExtraction" label="Start" class="p-button-sm" />
      </div>
    </div>
  </Panel>
</template>
<script>
import shotBouDetec from "../../provider/shotBouDetec";
import manFrame from "../../provider/manFrame";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../utils/config";

export default {
  name: "FrameExtraction",
  props: ["id", "filePath", "fileName"],

  data() {
    return {
      selectedMethod: null,
      slectedFrameExtrac: null,
      methodList: [
        {
          name: "Content Detector",
          value: 1,
        },
        { name: "Threshold Detector", value: 2 },
      ],
    };
  },

  methods: {
    onFrameExtraction() {
      if (this.slectedFrameExtrac == 1) {
        if (this.selectedMethod == null) {
          ipcRenderer.send(
            ipcKeys.mainAppFieldEmpty,
            "Select a method before start"
          );
        } else if (this.slectedFrameExtrac == 1 && this.thrValue == undefined) {
          ipcRenderer.send(
            ipcKeys.mainAppFieldEmpty,
            "Field cannot be empty on threshold"
          );
        } else {
          ipcRenderer.send(ipcKeys.mainAppLoading, "loadnow");
          setTimeout(() => {
            shotBouDetec(
              (data) => {
                if (data["data"] == "completed") {
                  ipcRenderer.send(ipcKeys.getGallary);
                }
              },
              this.$route.params.fileName,
              this.selectedMethod,
              this.thrValue,
              this.newHeight,
              this.newWidth
            );
          }, 1000);
        }
      } else if (this.slectedFrameExtrac == 2) {
        if (this.secValue == undefined) {
          ipcRenderer.send(
            ipcKeys.mainAppFieldEmpty,
            "Field cannot be empty on per second"
          );
        } else {
          ipcRenderer.send(ipcKeys.mainAppLoading, "loadnow");
          setTimeout(() => {
            manFrame(
              (data) => {
                if (data["data"] == "completed") {
                  ipcRenderer.send(ipcKeys.getGallary);
                }
              },
              this.$route.params.fileName,
              this.secValue,
              this.newHeight,
              this.newWidth
            );
          }, 1000);
        }
      }
    },
  },
};
</script>
<style scoped>
.fe-panel {
  padding-top: 30px;
}
.radio-label {
  padding-left: 15px;
}
.p-field-checkbox-b {
  padding-top: 10px;
}
.p-col {
  padding-top: 12px;
  padding-bottom: 15px;
}
.p-col-3 {
  padding-top: 15px;
  padding-bottom: 15px;
}

.img-res {
  padding-bottom: 25px;
}

.p-slider-horizontal,
.p-inputtext {
  width: 18rem;
}
</style>
