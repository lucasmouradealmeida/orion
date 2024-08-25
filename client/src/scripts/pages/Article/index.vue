<template>
  <div class="mx-auto mt-4 max-w-4xl rounded-lg p-6">
    <h1 class="mb-4 text-3xl font-bold text-white">{{ titulo }}</h1>

    <div v-for="(value, key) in sortedContent" :key="key" class="mb-6">
      <h2 class="mb-2 text-2xl font-semibold text-white">{{ formatKey(key) }}</h2>

      <div v-if="value.image" class="mb-4 flex justify-center">
        <img :src="value.image" alt="section image" class="w-full rounded-lg" />
      </div>

      <p class="whitespace-pre-line text-lg leading-relaxed text-white">
        {{ value.descricao }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Article',
  data() {
    return {
      title: '',
      content: '',
      id: window.__site__.context.id,
      titulo: window.__site__.context.titulo,
      conteudo: window.__site__.context.conteudo
    }
  },
  computed: {
    sortedContent() {
      // Ordena as chaves do objeto com base no sufixo numérico
      return Object.keys(this.conteudo)
        .sort((a, b) => {
          const numA = parseInt(a.split('_').pop())
          const numB = parseInt(b.split('_').pop())
          return numA - numB
        })
        .reduce((sorted, key) => {
          sorted[key] = this.conteudo[key]
          return sorted
        }, {})
    }
  },
  methods: {
    formatKey(key) {
      // Formata a chave removendo o sufixo numérico e substituindo "_" por espaços
      const formatted = key.split('_')[0]
      return formatted.charAt(0).toUpperCase() + formatted.slice(1)
    }
  }
}
</script>

<style scoped>
.max-w-4xl {
  max-width: 64rem;
}
.leading-relaxed {
  line-height: 1.75;
}
</style>
