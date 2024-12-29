<template>
  <div class="alert-stack">
    <transition-group name="slide" tag="div">
      <div v-for="alert in alerts" :key="alert.id" role="alert" :class="`alert-container my-1 ${alert.type}`">
        <div class="icon">
          <!-- SVG Dinâmico com base no tipo de alerta -->
          <svg
            v-if="alert.type == 'info'"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            class="stroke-current h-6 w-6 shrink-0"
            style="stroke: white">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <svg
            v-if="alert.type === 'warning'"
            xmlns="http://www.w3.org/2000/svg"
            class="stroke-current h-6 w-6 shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            style="stroke: white">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
          </svg>
          <svg
            v-if="alert.type === 'success'"
            xmlns="http://www.w3.org/2000/svg"
            class="stroke-current h-6 w-6 shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            style="stroke: white">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <svg
            v-if="alert.type === 'error'"
            xmlns="http://www.w3.org/2000/svg"
            class="stroke-current h-6 w-6 shrink-0"
            fill="none"
            viewBox="0 0 24 24"
            style="stroke: white">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </div>
        <span>{{ alert.message }}</span>
        <button @click="closeAlert(alert.id)">x</button>
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  data() {
    return {
      alerts: [],
      idCounter: 0
    }
  },
  methods: {
    // Adiciona um novo alerta à fila
    addAlert(type, message, timer = 5000) {
      const newAlert = {
        id: this.idCounter++,
        type,
        message,
        timer
      }

      this.alerts.push(newAlert)

      // Fecha o alerta automaticamente após o tempo configurado
      setTimeout(() => {
        this.closeAlert(newAlert.id)
      }, timer)
    },

    // Método para ser chamado externamente para disparar um alerta
    triggerAlert(type, message, timer = 5000) {
      this.addAlert(type, message, timer)
    },

    // Fecha o alerta com base no ID
    closeAlert(id) {
      this.alerts = this.alerts.filter((alert) => alert.id !== id)
    }
  }
}
</script>
