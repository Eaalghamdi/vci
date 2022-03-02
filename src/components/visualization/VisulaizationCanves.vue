<template>
  <div class="card">
    <canvas ref="productsBar" />
  </div>
</template>
<script>
import { Chart, registerables } from "chart.js";
import "chartjs-adapter-moment";
import { ipcRenderer } from "electron";
import { ipcKeys } from "../../utils/config";
import getObjectDetection from "../../provider/getObjectDetection";
import getColorFulness from "../../provider/getColorFulness";
import getStruSimilarity from "../../provider/getStruSimilarity";
import getCompression from "../../provider/getCompression";
import getFaceDetection from "../../provider/getFaceDetection";
import getEdgeDetection from "../../provider/getEdgeDetection";
import getMotion from "../../provider/getMotion";
import getSliency from "../../provider/getSliency";

export default {
  name: "VisulaizationCanves",
  props: ["id", "filePath", "fileName"],
  data() {
    return {};
  },
  created() {
    Chart.register(...registerables);
  },

  mounted() {
    let ctx = this.$refs.productsBar.getContext("2d");
    ipcRenderer.on(ipcKeys.panelVisibilityAck, (event, data) => {
      if (data[0] == "showORPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getObjectDetection((fetchData) => {
          // this.products = data;
          let classIndex = [];
          let confidence = [];
          let names = [];
          for (let i = 0; i < fetchData.length; i++) {
            classIndex.push(fetchData[i]["classindex"]);
            confidence.push(fetchData[i]["confidence"]);
            names.push(fetchData[i]["imgname"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Class Index",
                  backgroundColor: "#EC407A",
                  data: classIndex,
                },
                {
                  label: "Confidence",
                  backgroundColor: "#78909C",
                  data: confidence,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showCFPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getColorFulness((fetchData) => {
          let names = [];
          let meanColor = [];
          let stdColor = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(fetchData[i]["imgname"]);
            meanColor.push(fetchData[i]["meancolor"]);
            stdColor.push(fetchData[i]["stdcolor"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Mean Color",
                  backgroundColor: "#EC407A",
                  data: meanColor,
                },
                {
                  label: "Std Color",
                  backgroundColor: "#78909C",
                  data: stdColor,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showSSPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getStruSimilarity((fetchData) => {
          let names = [];
          let mse = [];
          let ssim = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(
              fetchData[i]["imganame"] + " - " + fetchData[i]["imgbname"]
            );
            mse.push(fetchData[i]["mse"]);
            ssim.push(fetchData[i]["ssim"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "MSE",
                  backgroundColor: "#EC407A",
                  data: mse,
                },
                {
                  label: "SSIM",
                  backgroundColor: "#78909C",
                  data: ssim,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showCOPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getCompression((fetchData) => {
          let names = [];
          let previousSize = [];
          let convertedSize = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(
              fetchData[i]["filename"] + " to " + fetchData[i]["cnvformat"]
            );
            previousSize.push(fetchData[i]["sizebytprev"]);
            convertedSize.push(fetchData[i]["sizebytnew"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Previous Size",
                  backgroundColor: "#EC407A",
                  data: previousSize,
                },
                {
                  label: "Converted Size",
                  backgroundColor: "#78909C",
                  data: convertedSize,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showFDPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getFaceDetection((fetchData) => {
          let names = [];
          let numfaces = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(fetchData[i]["filename"]);
            numfaces.push(fetchData[i]["numfaces"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Number of Facess",
                  backgroundColor: "#EC407A",
                  data: numfaces,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showEDPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getEdgeDetection((fetchData) => {
          let names = [];
          let meanval = [];
          let stdval = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(fetchData[i]["imgname"]);
            meanval.push(fetchData[i]["meanval"]);
            stdval.push(fetchData[i]["stdval"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Mean Value",
                  backgroundColor: "#EC407A",
                  data: meanval,
                },
                {
                  label: "Std Value",
                  backgroundColor: "#78909C",
                  data: stdval,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showMOPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getMotion((fetchData) => {
          let names = [];
          let movingdurationms = [];
          let ratioofmovingobjectsns = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(fetchData[i]["videoname"]);
            movingdurationms.push(fetchData[i]["movingdurationms"]);
            ratioofmovingobjectsns.push(fetchData[i]["ratioofmovingobjectsns"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Moving Duration (m/s)",
                  backgroundColor: "#EC407A",
                  data: movingdurationms,
                },
                {
                  label: "Ratio of Moving Objects (n/s)",
                  backgroundColor: "#78909C",
                  data: ratioofmovingobjectsns,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      } else if (data[0] == "showSAPlan") {
        let chartStatus = Chart.getChart(ctx);
        if (chartStatus != undefined) {
          chartStatus.destroy();
        }

        getSliency((fetchData) => {
          let names = [];
          let meanval = [];
          let stdval = [];
          for (let i = 0; i < fetchData.length; i++) {
            names.push(fetchData[i]["filename"]);
            meanval.push(fetchData[i]["mean"]);
            stdval.push(fetchData[i]["std"]);
          }
          new Chart(ctx, {
            type: data[1],
            options: {
              plugins: {
                legend: {
                  labels: {
                    color: "#495057",
                  },
                },
                tooltips: {
                  mode: "index",
                  intersect: true,
                },
              },
              scales: {
                x: {
                  ticks: {
                    color: "#495057",
                  },
                },
                y: {
                  ticks: {
                    color: "#495057",
                  },
                },
              },
            },
            data: {
              labels: names,
              datasets: [
                {
                  label: "Mean",
                  backgroundColor: "#EC407A",
                  data: meanval,
                },
                {
                  label: "Std",
                  backgroundColor: "#78909C",
                  data: stdval,
                },
              ],
            },
          });
          ipcRenderer.send(ipcKeys.mainAppLoading, "stopVis");
        });
      }
      ipcRenderer.removeListener(ipcKeys.panelVisibilityAck, () => {});
    });
  },
};
</script>
<style scoped>
.visCanvas {
  background-color: #1e1e1e;
}
</style>
