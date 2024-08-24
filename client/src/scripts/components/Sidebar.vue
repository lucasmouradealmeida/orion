<template>
  <div class="flex h-screen w-[220px] flex-col justify-between">
    <div class="w-[200px] px-4 py-6">
      <ul class="mt-6 space-y-3">
        <li v-for="item in menu" :key="item.name">
          <a
            v-if="!item.submenu"
            :href="item.url"
            :class="[
              'block cursor-pointer',
              currentView === item.url ? 'bg-gray-100 text-black' : 'text-white hover:bg-gray-100 hover:text-black',
              'flex items-center space-x-2 rounded-lg px-4 py-2'
            ]">
            <!-- Renderiza o ícone -->
            <svg
              class="h-6 w-6 text-gray-800 dark:text-white"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="none"
              viewBox="0 0 24 24">
              <path
                stroke="#222222"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m4 12 8-8 8 8M6 10.5V19a1 1 0 0 0 1 1h3v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h3a1 1 0 0 0 1-1v-8.5" />
            </svg>
            <span class="text-sm font-medium">{{ item.name }}</span>
          </a>

          <!-- Menu com Submenu -->
          <details v-else class="group [&_summary::-webkit-details-marker]:hidden">
            <summary
              :class="[
                'flex cursor-pointer items-center justify-between rounded-lg px-4 py-2',
                currentView.includes(item.url) ? 'text-black' : 'text-white hover:bg-gray-100 hover:text-black'
              ]">
              <svg
                class="h-6 w-6"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                fill="none"
                viewBox="0 0 24 24">
                <path
                  stroke="currentColor"
                  stroke-linejoin="round"
                  stroke-width="1.8"
                  d="M4 5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5Zm16 14a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2ZM4 13a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6Zm16-2a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v6Z" />
              </svg>
              <span class="text-sm font-medium">{{ item.name }}</span>

              <span class="w-[20px] shrink-0 transition duration-300 group-open:-rotate-180">
                <svg xmlns="http://www.w3.org/2000/svg" class="size-5" viewBox="0 0 20 20" fill="currentColor">
                  <path
                    fill-rule="evenodd"
                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                    clip-rule="evenodd" />
                </svg>
              </span>
            </summary>

            <ul class="mt-2 space-y-1 px-4">
              <li v-for="submenuItem in item.submenu" :key="submenuItem.name">
                <a
                  :href="submenuItem.url"
                  :class="[
                    'block rounded-lg px-4 py-2 text-sm font-medium',
                    currentView === submenuItem.url
                      ? 'bg-gray-100 text-black'
                      : 'text-white hover:bg-gray-100 hover:text-black'
                  ]">
                  {{ submenuItem.name }}
                </a>
              </li>
            </ul>
          </details>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: this.$jinjaContext.menu,
      currentView: this.$jinjaContext.currentView
    }
  }
}
</script>
