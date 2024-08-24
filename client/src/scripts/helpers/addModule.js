import { createApp } from 'vue'
import store from '@/store'
import { hasElement } from '@/helpers'
import { Context } from '@/plugins/'

const addModule = (ref, Module) => {
  const isThere = hasElement(ref)

  if (isThere) {
    const app = createApp(Module)
    app.use(store)

    // Install plugins before mounting
    installPlugins(app)

    app.mount(ref)
  }
}

function installPlugins(app) {
  app.use(Context)
  store.state.jinjaContext = app.config.globalProperties.$jinjaContext
}

export default addModule
