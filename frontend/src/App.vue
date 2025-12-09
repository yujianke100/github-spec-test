
<script setup>
import { ref } from 'vue'
import QueryForm from './components/QueryForm.vue'
import StatsCharts from './components/StatsCharts.vue'
import { queryStats } from './api/index.js'

const stats = ref(null)
const loading = ref(false)
const error = ref('')

function handleQuery(params) {
  stats.value = null
  error.value = ''
  loading.value = true
  queryStats(params)
    .then(res => {
      stats.value = res.data
      if (!res.data.prices.length) error.value = '无数据'
    })
    .catch(e => {
      error.value = e.response?.data?.error || '查询失败'
    })
    .finally(() => loading.value = false)
}
</script>

<template>
  <div style="max-width:700px;margin:40px auto;padding:24px;background:#fff;border-radius:8px;box-shadow:0 2px 8px #eee;">
    <h2 style="margin-bottom:24px;">股票统计查询</h2>
    <QueryForm @query="handleQuery" />
    <StatsCharts :stats="stats" :loading="loading" :error="error" style="margin-top:32px;" />
  </div>
</template>

<style scoped>
body {
  background: #f5f6fa;
}
</style>
