import '@styles'

import { addModule } from '@/helpers'
import { Sidebar, menuDrawer, Footer, userActions } from '@/components'

addModule('#module-sidebar', Sidebar)
addModule('#module-menu-drawer', menuDrawer)
addModule('#module-footer', Footer)
addModule('#module-user-actions', userActions)
