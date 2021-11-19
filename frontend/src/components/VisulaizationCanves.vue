<template>
  <div class="p-col">
    <Chart class="visCanvas" type="line" :data="basicData" :options="options" />
  </div>
</template>
<script>
export default {
  name: "VisulaizationCanves",
  data() {
    return {
      basicData: {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        datasets: [
          {
            label: "Colorfulness",
            data: [65, 59, 80, 81, 56, 55, 40, 59, 80, 81, 22, 26],
            fill: false,
            borderColor: "#2E8B57",
          },
          {
            label: "Number of  Obejcts",
            data: [28, 48, 40, 19, 86, 27, 30, 28, 28, 40, 19, 86],
            fill: true,
            borderColor: "#FFA726",
          },
        ],
      },
    };
  },
  options: {
    responsive: true,
    hoverMode: "index",
    stacked: false,
    scales: {
      yAxes: [
        {
          type: "linear",
          display: true,
          position: "left",
          id: "y-axis-1",
        },
        {
          type: "linear",
          display: true,
          position: "right",
          id: "y-axis-2",
          gridLines: {
            drawOnChartArea: true,
          },
        },
      ],
    },
  },
};
</script>
<style scoped>
.visCanvas {
  background-colr: #1e1e1e;
}
</style>
