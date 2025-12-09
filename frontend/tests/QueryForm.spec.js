import { mount } from '@vue/test-utils'
import QueryForm from '../src/components/QueryForm.vue'

describe('QueryForm', () => {
  it('初始渲染应有股票选择', () => {
    const wrapper = mount(QueryForm, {
      global: {
        mocks: {
          axios: { get: () => Promise.resolve({ data: [{ stock_id: 1, name: 'Stock01' }] }) }
        }
      }
    })
    expect(wrapper.html()).toContain('股票')
  })
})
