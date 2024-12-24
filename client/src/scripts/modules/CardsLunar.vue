<template>
  <div class="w-full px-8">
    <div
      v-for="(curve, index) in curves"
      :key="index"
      class="mb-4 flex items-center justify-between rounded-lg border p-4 text-white">
      <div v-if="curve.tipo == 1">
        <p class="font-bold">{{ curve.nome }}</p>

        <div class="space-x-4">
          <span class="text-base">Massa: {{ curve.massa }}</span>
          <span class="text-base">Gravidade: {{ curve.gravidade }}</span>
          <span class="text-base">Intensidade: {{ curve.intensidade }}</span>
          <span class="text-base">Angulação: {{ curve.angulacao }}</span>
        </div>
      </div>
      <div v-else>
        <p class="font-bold">{{ curve.nome }}</p>

        <div class="space-x-4">
          <span class="text-base">Altura: {{ curve.altura }}</span>
          <span class="text-base">Velocidade Inicial: {{ curve.velocidade_inicial }}</span>
        </div>
      </div>
      <button @click="removeCurve(index)" aria-label="Remove Curve">
        <svg
          class="h-6 w-6 text-white"
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
            d="M5 7h14m-9 3v8m4-8v8M10 3h4a1 1 0 0 1 1 1v3H9V4a1 1 0 0 1 1-1ZM6 7h12v13a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7Z" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    curves: {
      type: Array,
      required: true
    }
  },
  methods: {
    removeCurve(index) {
      this.$emit('remove-curve', index)
    }
  }
}
</script>
