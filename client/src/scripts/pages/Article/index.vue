<template>
  <div class="mx-auto mt-4 max-w-4xl rounded-lg p-6">
    <h1 class="mb-4 text-3xl font-bold text-white">{{ titulo }}</h1>
    <p class="whitespace-pre-line text-lg leading-relaxed text-white">
      {{ conteudo }}
    </p>
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
