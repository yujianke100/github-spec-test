import { mount } from '@vue/test-utils'
import StatsCharts from '../src/components/StatsCharts.vue'

describe('StatsCharts', () => {
  it('显示无数据', () => {
    const wrapper = mount(StatsCharts, {
      props: { stats: { prices: [] }, loading: false, error: '' }
    })
    expect(wrapper.text()).toContain('无数据')
  })

  it('显示加载中', () => {
    const wrapper = mount(StatsCharts, {
      props: { stats: null, loading: true, error: '' }
    })
    expect(wrapper.text()).toContain('加载中')
  })

  it('显示错误信息', () => {
    const wrapper = mount(StatsCharts, {
      props: { stats: null, loading: false, error: '出错了' }
    })
    expect(wrapper.text()).toContain('出错了')
  })
})
