import axios from 'axios'

export function queryStats(params) {
  return axios.post('/api/query', params)
}
