<template>
  <div class="mb-10 px-6">
    <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Artigos</div>

    <div class="grid grid-cols-1 gap-4 p-4 sm:grid-cols-2 lg:grid-cols-3">
      <div v-for="artigo in artigos">
        <article class="rounded-lg border border-gray-100 bg-white p-4 transition sm:p-6">
          <span class="inline-block rounded bg-[#324AB2] p-2 text-white">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-[20px] w-[20px]"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor">
              <path d="M12 14l9-5-9-5-9 5 9 5z" />
              <path
                d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" />
            </svg>
          </span>

          <a>
            <h3 class="mt-0.5 text-lg font-bold text-gray-900">{{ artigo.titulo }}</h3>
          </a>

          <p class="mt-2 line-clamp-3 text-sm text-black">{{ artigo.conteudo['introducao_1']['descricao'] }}</p>

          <a
            :href="'/article/' + artigo.id"
            class="text-blue-600 group mt-4 inline-flex items-center gap-1 text-sm font-medium">
            Leia mais
            <span aria-hidden="true" class="block transition-all group-hover:ms-0.5 rtl:rotate-180">&rarr;</span>
          </a>
        </article>
      </div>
    </div>
  </div>
</template>
<script>
import Modal from '@/components/Modal'
import UserModal from '@/components/UserModal'
import LineChart from '../../modules/LineChart.vue'
import _ from 'lodash'

export default {
  name: 'Home',
  components: {
    UserModal,
    Modal,
    LineChart
  },
  data() {
    return {
      artigos: window.__site__.context.artigos
    }
  }
}
</script>
