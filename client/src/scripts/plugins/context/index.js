import { reactive } from 'vue'

const Context = {
  install(app) {
    const jinjaContext = reactive(window.__site__.context || {})
    app.config.globalProperties.$jinjaContext = jinjaContext
  }
}

export default Context
