<template>
  <div v-if="loading">加载中...</div>
  <div v-else>
    <div v-if="error" style="color:red">{{ error }}</div>
    <div v-else-if="!stats || !stats.prices.length">无数据</div>
    <div v-else>
      <div style="height:300px;margin-bottom:16px;">
        <v-chart :option="priceOption" autoresize />
      </div>
      <div style="height:300px;margin-bottom:16px;">
        <v-chart :option="volumeOption" autoresize />
      </div>
      <div>总买入金额: {{ stats.pnl.total_buy.toFixed(2) }}，总卖出金额: {{ stats.pnl.total_sell.toFixed(2) }}，净盈亏: <span :style="{color: stats.pnl.net_profit >= 0 ? 'green' : 'red'}">{{ stats.pnl.net_profit.toFixed(2) }}</span></div>
    </div>
  </div>
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
    title: { text: '价格曲线' },
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: val.prices.map(p => p.time) },
    yAxis: { type: 'value' },
    series: [{ data: val.prices.map(p => p.price), type: 'line', smooth: true }]
  }
  volumeOption.value = {
    title: { text: '买卖量' },
    tooltip: { trigger: 'axis' },
    legend: { data: ['买入量', '卖出量'] },
    xAxis: { type: 'category', data: val.volumes.map(v => v.time) },
    yAxis: { type: 'value' },
    series: [
      { name: '买入量', data: val.volumes.map(v => v.buy_volume), type: 'bar' },
      { name: '卖出量', data: val.volumes.map(v => v.sell_volume), type: 'bar' }
    ]
  }
}, { immediate: true })
</script>
