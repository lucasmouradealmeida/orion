<template>
  <div class="mb-4" v-if="data.length > 0">
    <!-- Campo de pesquisa -->
    <div class="my-4 flex items-center justify-start">
      <!-- Select para escolher o campo -->
      <select v-model="searchField" class="mr-2 rounded-lg border border-gray-400 px-4 py-2">
        <option value="">Todos os campos</option>
        <option value="OBJECT_NAME">Object Name</option>
        <option value="OBJECT_ID">Object ID</option>
        <option value="ECCENTRICITY">Eccentricity</option>
        <option value="INCLINATION">Inclination</option>
        <option value="ARG_OF_PERICENTER">Arg of Pericenter</option>
      </select>

      <!-- Container com ícone SVG e input -->
      <div class="relative w-1/2">
        <!-- Ícone de lupa -->
        <svg
          class="absolute left-3 top-1/2 -translate-y-1/2 transform text-gray-500"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          width="22"
          height="22"
          fill="none"
          viewBox="0 0 24 24">
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-width="2"
            d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z" />
        </svg>

        <!-- Input com padding ajustado para o ícone -->
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Digite para pesquisar..."
          class="focus:ring-blue-500 w-full rounded-lg border border-gray-400 px-10 py-2 focus:outline-none focus:ring-2" />
      </div>
    </div>

    <div class="table-container">
      <!-- Verificar se há dados -->
      <div v-if="filteredData.length > 0" class="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="(row, index) in paginatedData"
          :key="index"
          class="card relative rounded-lg bg-[#3b3b3b] p-6 shadow-md">
          <!-- Título do card (OBJECT_NAME) -->
          <div class="mb-4 w-max rounded-lg bg-[#324AB2] p-2">
            <h2 class="mx-1 text-center text-base font-bold text-white">{{ row.OBJECT_NAME }}</h2>
          </div>

          <!-- Dados principais -->
          <p class="mb-2 rounded-md text-white">
            <strong>Object ID:</strong>
            {{ row.OBJECT_ID }}
          </p>
          <p class="mb-2 rounded-md text-white">
            <strong>Eccentricity:</strong>
            {{ row.ECCENTRICITY }}
          </p>
          <p class="mb-2 rounded-md text-white">
            <strong>Inclination:</strong>
            {{ row.INCLINATION }}°
          </p>
          <p class="mb-2 rounded-md text-white">
            <strong>Arg of Pericenter:</strong>
            {{ row.ARG_OF_PERICENTER }}
          </p>

          <!-- Botão para abrir modal -->
          <div @click="openModal(row)" class="mt-4 flex w-max cursor-pointer flex-row rounded-md bg-gray-100 p-2">
            <a class="bg-blue-500 hover:bg-blue-700 rounded-lg font-bold text-[#324AB2]">Ver mais</a>
            <svg
              class="ml-2 h-6 w-6 text-[#324AB2]"
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
                d="M19 12H5m14 0-4 4m4-4-4-4" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Paginação -->
    <div class="pagination mt-4 flex items-center justify-center" v-if="filteredData.length > 0">
      <a
        @click="prevPage"
        :disabled="currentPage === 1"
        :class="{
          'cursor-not-allowed opacity-50': currentPage === 1,
          'bg-[#3b3b3b] text-white': currentPage === 1,
          'hover:bg-blue-500 bg-[#3b3b3b] text-white': currentPage > 1
        }"
        class="mx-1 flex cursor-pointer items-center justify-center rounded-md px-4 py-2 capitalize transition-colors duration-300 rtl:-scale-x-100">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path
            fill-rule="evenodd"
            d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
            clip-rule="evenodd" />
        </svg>
      </a>

      <div class="flex items-center">
        <template v-for="page in pagesToShow" :key="page">
          <a
            @click="setPage(page)"
            :class="{
              'bg-[#324AB2] text-white': page === currentPage,
              'hover:bg-blue-500 bg-[#3b3b3b] text-white': page !== currentPage
            }"
            class="mx-1 flex cursor-pointer items-center justify-center rounded-md px-4 py-2 transition-colors duration-300 rtl:-scale-x-100">
            {{ page }}
          </a>
        </template>
      </div>

      <a
        @click="nextPage"
        :disabled="currentPage === totalPages"
        :class="{
          'cursor-not-allowed opacity-50': currentPage === totalPages,
          'bg-[#3b3b3b] text-white': currentPage === totalPages,
          'hover:bg-blue-500 bg-[#3b3b3b] text-white': currentPage < totalPages
        }"
        class="mx-1 flex cursor-pointer items-center justify-center rounded-md px-4 py-2 transition-colors duration-300 rtl:-scale-x-100">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
          <path
            fill-rule="evenodd"
            d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
            clip-rule="evenodd" />
        </svg>
      </a>
    </div>

    <!-- Modal para ver mais detalhes -->
    <Modal v-if="showModal" @close="showModal = false">
      <template #header>
        <h3 class="text-xl font-bold">{{ modalData.OBJECT_NAME }}</h3>
      </template>
      <template #body>
        <div class="m-4">
          <p class="mb-2">
            <strong>Object ID:</strong>
            {{ modalData.OBJECT_ID }}
          </p>
          <p class="mb-2">
            <strong>Eccentricity:</strong>
            {{ modalData.ECCENTRICITY }}
          </p>
          <p class="mb-2">
            <strong>Inclination:</strong>
            {{ modalData.INCLINATION }}°
          </p>
          <p class="mb-2">
            <strong>Arg of Pericenter:</strong>
            {{ modalData.ARG_OF_PERICENTER }}
          </p>
          <p class="mb-2">
            <strong>Mean Motion:</strong>
            {{ modalData.MEAN_MOTION }}
          </p>
          <p class="mb-2">
            <strong>RA of Asc Node:</strong>
            {{ modalData.RA_OF_ASC_NODE }}
          </p>
          <p class="mb-2">
            <strong>Mean Anomaly:</strong>
            {{ modalData.MEAN_ANOMALY }}
          </p>
          <p class="mb-2">
            <strong>Ephemeris Type:</strong>
            {{ modalData.EPHEMERIS_TYPE }}
          </p>
          <p class="mb-2">
            <strong>NORAD Cat ID:</strong>
            {{ modalData.NORAD_CAT_ID }}
          </p>
        </div>

        <!-- Adicionar mais campos conforme necessário -->
      </template>
      <template #footer></template>
    </Modal>
  </div>

  <!-- Mensagem caso não haja dados filtrados -->
  <div class="flex justify-center text-[20px] font-bold text-white" v-else>
    <p>Sem dados disponíveis</p>
  </div>
</template>

<script>
import Modal from '@/components/Modal'

export default {
  components: {
    Modal
  },
  props: {
    data: {
      type: Array,
      required: true
    },
    itemsPerPage: {
      type: Number,
      default: 9 // Ajustar para múltiplos de 3 por página
    }
  },
  data() {
    return {
      currentPage: 1,
      searchQuery: '', // Texto de pesquisa
      searchField: '', // Campo de pesquisa selecionado
      showModal: false,
      modalData: {} // Dados completos para exibir no modal
    }
  },
  computed: {
    pagesToShow() {
      const totalPages = this.totalPages
      const currentPage = this.currentPage

      // Cria uma lista de páginas para mostrar
      let startPage = Math.max(1, currentPage - 2)
      let endPage = Math.min(totalPages, currentPage + 2)

      // Limita o número total de páginas mostradas
      if (endPage - startPage < 4) {
        if (startPage === 1) {
          endPage = Math.min(5, totalPages)
        } else if (endPage === totalPages) {
          startPage = Math.max(1, totalPages - 4)
        }
      }

      return Array.from({ length: endPage - startPage + 1 }, (v, i) => i + startPage)
    },
    filteredData() {
      if (!this.searchQuery) {
        return this.data
      } else {
        this.currentPage = 1
      }

      return this.data.filter((row) => {
        if (this.searchField) {
          // Filtrar por campo específico
          return (
            row[this.searchField] &&
            row[this.searchField].toString().toLowerCase().includes(this.searchQuery.toLowerCase())
          )
        } else {
          // Filtrar por todos os campos
          return Object.keys(row).some((key) =>
            row[key].toString().toLowerCase().includes(this.searchQuery.toLowerCase())
          )
        }
      })
    },
    totalPages() {
      return Math.ceil(this.filteredData.length / this.itemsPerPage) || 1 // Garantir ao menos 1 página
    },
    paginatedData() {
      if (this.filteredData.length === 0) return []
      const start = (this.currentPage - 1) * this.itemsPerPage
      const end = start + this.itemsPerPage
      return this.filteredData.slice(start, end)
    }
  },
  methods: {
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--
      }
    },
    setPage(page) {
      this.currentPage = page
    },
    openModal(row) {
      this.modalData = row
      this.showModal = true
    }
  }
}
</script>
