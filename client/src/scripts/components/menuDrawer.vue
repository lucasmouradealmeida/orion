<template>
  <div class="text-white" @click="handleSidebar">
    <svg
      v-if="!sidebarActive"
      class="h-[30px] w-[30px]"
      aria-hidden="true"
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      fill="none"
      viewBox="0 0 24 24">
      <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M5 7h14M5 12h14M5 17h14" />
    </svg>

    <svg
      v-if="sidebarActive"
      class="h-[30px] w-[30px]"
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
        d="m15 9-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
    </svg>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sidebarActive: false,
      sidebarContainer: document.querySelector('.sidebar'),
      body: document.querySelector('body')
    }
  },
  methods: {
    handleSidebar() {
      if (this.sidebarActive) {
        this.sidebarActive = false
        this.sidebarContainer.classList.remove('isOpen')
        this.body.classList.remove('overflow-hidden')
      } else {
        this.sidebarActive = true
        this.sidebarContainer.classList.add('isOpen')
        this.body.classList.add('overflow-hidden')
      }
    }
  }
}
</script>
