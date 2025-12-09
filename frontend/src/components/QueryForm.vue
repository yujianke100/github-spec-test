
<template>
  <form @submit.prevent="onSubmit">
    <div style="margin-bottom:8px;">
      <label>股票：</label>
      <select v-model="stockId" required>
        <option value="" disabled>请选择</option>
        <option v-for="s in stocks" :key="s.stock_id" :value="s.stock_id">{{ s.stock_id }} - {{ s.name }}</option>
      </select>
    </div>
    <div style="margin-bottom:8px;">
      <label>开始时间：</label>
      <input type="datetime-local" v-model="startTime" :min="minTime" :max="maxTime" :disabled="!minTime" required />
    </div>
    <div style="margin-bottom:8px;">
      <label>结束时间：</label>
      <input type="datetime-local" v-model="endTime" :min="minTime" :max="maxTime" :disabled="!minTime" required />
    </div>
    <button type="submit">查询</button>
    <span v-if="error" style="color:red; margin-left:8px;">{{ error }}</span>
  </form>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const stocks = ref([])
const stockId = ref('')
const startTime = ref('')
const endTime = ref('')
const error = ref('')
const minTime = ref('')
const maxTime = ref('')

// 时间格式转换: "2025-12-02 15:17:37.856577" => "2025-12-02T15:17"
function toDatetimeLocal(str) {
  if (!str) return ''
  // 兼容有无毫秒
  const [date, time] = str.split(' ')
  return date + 'T' + time.slice(0,5)
}

onMounted(async () => {
  try {
    const res = await axios.get('/api/stocks')
    // 过滤无效项，确保stock_id和name存在
    stocks.value = (res.data || []).filter(s => s.stock_id && s.name)
  } catch (e) {
    error.value = '无法获取股票列表'
  }
})

watch(stockId, async (val) => {
  minTime.value = ''
  maxTime.value = ''
  startTime.value = ''
  endTime.value = ''
  if (!val) return
  try {
    const resp = await axios.post('/api/query', {
      stock_id: val,
      start_time: '1970-01-01T00:00',
      end_time: '2100-01-01T00:00'
    })
    const prices = resp.data.prices
    if (prices.length) {
      minTime.value = toDatetimeLocal(prices[0].time)
      maxTime.value = toDatetimeLocal(prices[prices.length-1].time)
    } else {
      error.value = '该股票无价格数据'
    }
  } catch {
    minTime.value = ''
    maxTime.value = ''
    error.value = '获取时间区间失败'
  }
})

const emit = defineEmits(['query'])

function onSubmit() {
  error.value = ''
  if (!stockId.value || !startTime.value || !endTime.value) {
    error.value = '请填写所有字段'
    return
  }
  if (endTime.value < startTime.value) {
    error.value = '结束时间不能早于开始时间'
    return
  }
  emit('query', {
    stock_id: stockId.value,
    start_time: startTime.value,
    end_time: endTime.value
  })
}
</script>
