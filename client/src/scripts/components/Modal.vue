<template>
  <div class="modal-backdrop" @click.self="close" tabindex="0" @keydown.esc="close">
    <div class="modal-back">
      <header class="modal-header">
        <div class="flex w-full items-center justify-between">
          <div class="flex-1 text-center">
            <slot name="header"></slot>
          </div>
          <svg
            @click="close"
            class="h-[30px] w-[30px] cursor-pointer"
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
      </header>

      <section class="modal-body">
        <slot name="body"></slot>
      </section>

      <footer class="modal-footer">
        <slot name="footer"></slot>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  mounted() {
    document.addEventListener('keydown', this.handleKeydown)
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.handleKeydown)
  },
  methods: {
    close() {
      this.$emit('close')
      document.querySelector('body').style.overflow = 'auto'
    },
    handleKeydown(event) {
      if (event.key === 'Escape') {
        this.close()
      }
    }
  }
}
</script>

<style scoped>
.modal-backdrop {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

.modal-back {
  @apply h-full lg:h-fit;

  background-color: white;
  padding: 1rem;
  border-radius: 8px;
  max-width: 100%;
  width: 600px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-btn {
  background: none;
  border: none;
  cursor: pointer;
}

.modal-body {
  margin-top: 1rem;
}

.modal-footer {
  margin-top: 1rem;
  text-align: right;
}
</style>
