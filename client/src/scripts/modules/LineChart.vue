<template>
  <div class="m-auto min-h-[600px] min-w-[350px]">
    <canvas class="rounded-lg bg-white p-5" ref="chart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)

export default {
  extends: Chart,
  data() {
    return {}
  },
  mounted() {
    this.chart = new Chart(this.$refs.chart, {
      type: 'line',
      data: this.chartData,
      options: this.options
    })
  },
  methods: {
    update() {
      this.chart.update()
    }
  },
  props: {
    chartData: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  }
}
</script>
