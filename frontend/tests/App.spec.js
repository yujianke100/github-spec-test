import { mount } from '@vue/test-utils'
import App from '../src/App.vue'

describe('App', () => {
  it('主页面包含标题', () => {
    const wrapper = mount(App)
    expect(wrapper.text()).toContain('股票统计查询')
  })
})
