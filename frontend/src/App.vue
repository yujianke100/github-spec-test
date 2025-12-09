
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
  <div class="app-bg">
    <header class="app-header">
      <h1>股票市场数据统计</h1>
      <span class="app-desc">本地虚拟数据 · 极速查询 · 动画展示</span>
    </header>
    <main class="app-main">
      <section class="app-card">
        <QueryForm @query="handleQuery" />
        <transition name="fade-slide" mode="out-in">
          <StatsCharts :stats="stats" :loading="loading" :error="error" style="margin-top:32px;" />
        </transition>
      </section>
    </main>
    <footer class="app-footer">
      <span>© 2025 股票市场数据统计演示 | 技术栈：Flask + Vue3 + ECharts</span>
    </footer>
  </div>
</template>

<style scoped>
.app-bg {
  min-height: 100vh;
  background: linear-gradient(120deg, #f5f6fa 60%, #e3e9f7 100%);
  display: flex;
  flex-direction: column;
}
.app-header {
  padding: 32px 0 12px 0;
  text-align: center;
  background: transparent;
}
.app-header h1 {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: 2px;
}
.app-desc {
  color: #888;
  font-size: 1rem;
}
.app-main {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: 600px;
}
.app-card {
  width: 100%;
  max-width: 900px;
  min-width: 600px;
  margin: 32px 0 24px 0;
  padding: 40px 40px 32px 40px;
  background: #fff;
  border-radius: 14px;
  box-shadow: 0 4px 24px #e3e9f7;
  transition: box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.app-card:hover {
  box-shadow: 0 8px 32px #d0d8ee;
}
@media (max-width: 900px) {
  .app-card {
    min-width: 0;
    max-width: 98vw;
    padding: 24px 6vw 18px 6vw;
  }
}
.app-footer {
  text-align: center;
  color: #aaa;
  font-size: 0.95rem;
  padding: 18px 0 10px 0;
}
/* 动画 */
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
