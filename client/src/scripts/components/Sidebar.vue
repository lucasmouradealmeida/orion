<template>
  <div class="flex h-screen w-[240px] flex-col justify-between">
    <div class="w-[220px] px-4 py-6">
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
              class="h-6 w-6"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="none"
              viewBox="0 0 24 24">
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m4 12 8-8 8 8M6 10.5V19a1 1 0 0 0 1 1h3v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h3a1 1 0 0 0 1-1v-8.5" />
            </svg>
            <span class="text-sm font-medium">{{ item.name }}</span>
          </a>

          <!-- Menu com Submenu -->
          <details v-else class="group [&_summary::-webkit-details-marker]:hidden" :open="isSubmenuOpen(item)">
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
                <div
                  :class="[
                    'block flex flex-row space-x-2 rounded-lg px-4 py-2 text-sm font-medium',
                    currentView === submenuItem.url
                      ? 'bg-gray-100 text-black'
                      : 'text-white hover:bg-gray-100 hover:text-black'
                  ]">
                  <svg
                    v-if="submenuItem.icon == 'pousolunar'"
                    width="20px"
                    height="20px"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                      d="M21.0672 11.8568L20.4253 11.469L21.0672 11.8568ZM12.1432 2.93276L11.7553 2.29085V2.29085L12.1432 2.93276ZM7.37554 20.013C7.017 19.8056 6.5582 19.9281 6.3508 20.2866C6.14339 20.6452 6.26591 21.104 6.62446 21.3114L7.37554 20.013ZM2.68862 17.3755C2.89602 17.7341 3.35482 17.8566 3.71337 17.6492C4.07191 17.4418 4.19443 16.983 3.98703 16.6245L2.68862 17.3755ZM21.25 12C21.25 17.1086 17.1086 21.25 12 21.25V22.75C17.9371 22.75 22.75 17.9371 22.75 12H21.25ZM2.75 12C2.75 6.89137 6.89137 2.75 12 2.75V1.25C6.06294 1.25 1.25 6.06294 1.25 12H2.75ZM15.5 14.25C12.3244 14.25 9.75 11.6756 9.75 8.5H8.25C8.25 12.5041 11.4959 15.75 15.5 15.75V14.25ZM20.4253 11.469C19.4172 13.1373 17.5882 14.25 15.5 14.25V15.75C18.1349 15.75 20.4407 14.3439 21.7092 12.2447L20.4253 11.469ZM9.75 8.5C9.75 6.41182 10.8627 4.5828 12.531 3.57467L11.7553 2.29085C9.65609 3.5593 8.25 5.86509 8.25 8.5H9.75ZM12 2.75C11.9115 2.75 11.8077 2.71008 11.7324 2.63168C11.6686 2.56527 11.6538 2.50244 11.6503 2.47703C11.6461 2.44587 11.6482 2.35557 11.7553 2.29085L12.531 3.57467C13.0342 3.27065 13.196 2.71398 13.1368 2.27627C13.0754 1.82126 12.7166 1.25 12 1.25V2.75ZM21.7092 12.2447C21.6444 12.3518 21.5541 12.3539 21.523 12.3497C21.4976 12.3462 21.4347 12.3314 21.3683 12.2676C21.2899 12.1923 21.25 12.0885 21.25 12H22.75C22.75 11.2834 22.1787 10.9246 21.7237 10.8632C21.286 10.804 20.7293 10.9658 20.4253 11.469L21.7092 12.2447ZM12 21.25C10.3139 21.25 8.73533 20.7996 7.37554 20.013L6.62446 21.3114C8.2064 22.2265 10.0432 22.75 12 22.75V21.25ZM3.98703 16.6245C3.20043 15.2647 2.75 13.6861 2.75 12H1.25C1.25 13.9568 1.77351 15.7936 2.68862 17.3755L3.98703 16.6245Z"
                      fill="currentColor" />
                  </svg>

                  <svg
                    v-if="submenuItem.icon == 'twolines'"
                    class="h-[20px] w-[20px]"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    width="25"
                    height="25"
                    fill="none"
                    viewBox="0 0 25 25">
                    <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M5 12h14M5 17h10" />
                  </svg>

                  <a :href="submenuItem.url">
                    {{ submenuItem.name }}
                  </a>
                </div>
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
  },
  methods: {
    isSubmenuOpen(item) {
      return item.submenu && item.submenu.some((submenuItem) => submenuItem.url === this.currentView)
    }
  }
}
</script>
