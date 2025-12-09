<template>
  <transition name="fade-slide" mode="out-in">
    <div v-if="loading" key="loading" class="chart-loading">加载中...</div>
    <div v-else key="content">
      <div v-if="error" class="chart-error">{{ error }}</div>
      <div v-else-if="!stats || !stats.prices.length" class="chart-empty">无数据</div>
      <div v-else>
        <div class="chart-block">
          <v-chart :option="priceOption" autoresize class="chart-echart" />
        </div>
        <div class="chart-block">
          <v-chart :option="volumeOption" autoresize class="chart-echart" />
        </div>
        <div class="chart-pnl">
          <span>总买入金额: <b>{{ stats.pnl.total_buy.toFixed(2) }}</b></span>
          <span>总卖出金额: <b>{{ stats.pnl.total_sell.toFixed(2) }}</b></span>
          <span>净盈亏: <b :style="{color: stats.pnl.net_profit >= 0 ? 'green' : 'red'}">{{ stats.pnl.net_profit.toFixed(2) }}</b></span>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, watch } from 'vue'
import { use } from 'echarts/core'
import VChart from 'vue-echarts'
import { LineChart, BarChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, GridComponent, LegendComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

use([LineChart, BarChart, TitleComponent, TooltipComponent, GridComponent, LegendComponent, CanvasRenderer])

const props = defineProps({
  stats: Object,
  loading: Boolean,
  error: String
})

const priceOption = ref({})
const volumeOption = ref({})

watch(() => props.stats, (val) => {
  if (!val || !val.prices) return
  priceOption.value = {
    title: { text: '价格曲线', left: 'center', textStyle: { fontWeight: 600 } },
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: val.prices.map(p => p.time), boundaryGap: false },
    yAxis: { type: 'value' },
    series: [{ data: val.prices.map(p => p.price), type: 'line', smooth: true, areaStyle: {}, symbol: 'circle', symbolSize: 6, lineStyle: { width: 3 } }],
    animationDuration: 800
  }
  volumeOption.value = {
    title: { text: '买卖量', left: 'center', top: 10, textStyle: { fontWeight: 600 } },
    tooltip: { trigger: 'axis' },
    legend: { data: ['买入量', '卖出量'], top: 38, left: 'center', orient: 'horizontal' },
    grid: { top: 70, left: 40, right: 20, bottom: 40 },
    xAxis: { type: 'category', data: val.volumes.map(v => v.time), boundaryGap: true },
    yAxis: { type: 'value' },
    series: [
      { name: '买入量', data: val.volumes.map(v => v.buy_volume), type: 'bar', itemStyle: { color: '#4caf50' }, barWidth: 10, emphasis: { focus: 'series' } },
      { name: '卖出量', data: val.volumes.map(v => v.sell_volume), type: 'bar', itemStyle: { color: '#f44336' }, barWidth: 10, emphasis: { focus: 'series' } }
    ],
    animationDuration: 800
  }
}, { immediate: true })
</script>
<style scoped>
.chart-loading {
  text-align: center;
  color: #888;
  font-size: 1.2rem;
  padding: 48px 0;
}
.chart-error {
  color: #e53935;
  text-align: center;
  font-size: 1.1rem;
  padding: 32px 0;
}
.chart-empty {
  color: #aaa;
  text-align: center;
  font-size: 1.1rem;
  padding: 32px 0;
}
.chart-block {
  height: 300px;
  margin-bottom: 18px;
  background: #f8fafc;
  border-radius: 10px;
  box-shadow: 0 2px 8px #f0f2f8;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: box-shadow 0.3s;
}
.chart-block:hover {
  box-shadow: 0 6px 18px #e3e9f7;
}
.chart-echart {
  width: 100% !important;
  height: 100% !important;
}
.chart-pnl {
  margin-top: 10px;
  display: flex;
  gap: 24px;
  justify-content: center;
  font-size: 1.08rem;
  color: #333;
}
.chart-pnl b {
  font-weight: 600;
  margin: 0 2px;
}
/* 动画复用App.vue */
.fade-slide-enter-active, .fade-slide-leave-active {
  transition: all 0.5s cubic-bezier(.55,0,.1,1);
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(30px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}
</style>
