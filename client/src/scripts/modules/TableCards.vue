<template>
  <div v-if="data.length > 0">
    <!-- Campo de pesquisa -->
    <div class="search-container my-4 flex items-center justify-center">
      <!-- Select para escolher o campo -->
      <select v-model="searchField" class="mr-2 rounded-lg border border-gray-400 px-4 py-2">
        <option value="">Todos os campos</option>
        <option value="OBJECT_NAME">Object Name</option>
        <option value="OBJECT_ID">Object ID</option>
        <option value="ECCENTRICITY">Eccentricity</option>
        <option value="INCLINATION">Inclination</option>
        <option value="ARG_OF_PERICENTER">Arg of Pericenter</option>
        <!-- Adicionar mais opções conforme necessário -->
      </select>

      <!-- Input para o texto de pesquisa -->
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Digite para pesquisar..."
        class="w-1/2 rounded-lg border border-gray-400 px-4 py-2" />
    </div>

    <div class="table-container">
      <!-- Verificar se há dados -->
      <div v-if="filteredData.length > 0" class="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <div v-for="(row, index) in paginatedData" :key="index" class="card relative rounded-lg bg-white p-6 shadow-md">
          <!-- Título do card (OBJECT_NAME) -->
          <h2 class="text-blue-600 mb-4 text-center text-xl font-bold">{{ row.OBJECT_NAME }}</h2>

          <!-- Dados principais -->
          <p class="mb-2">
            <strong>Object ID:</strong>
            {{ row.OBJECT_ID }}
          </p>
          <p class="mb-2">
            <strong>Eccentricity:</strong>
            {{ row.ECCENTRICITY }}
          </p>
          <p class="mb-2">
            <strong>Inclination:</strong>
            {{ row.INCLINATION }}°
          </p>
          <p class="mb-2">
            <strong>Arg of Pericenter:</strong>
            {{ row.ARG_OF_PERICENTER }}
          </p>

          <!-- Botão para abrir modal -->
          <button
            @click="openModal(row)"
            class="bg-blue-500 hover:bg-blue-700 mt-4 rounded-lg px-4 py-2 font-bold text-white">
            Ver mais
          </button>
        </div>
      </div>

      <!-- Mensagem caso não haja dados filtrados -->
      <div v-else>
        <p>Sem dados disponíveis ou correspondentes à pesquisa.</p>
      </div>
    </div>

    <!-- Paginação -->
    <div class="pagination mt-4 flex items-center justify-center" v-if="filteredData.length > 0">
      <button
        @click="prevPage"
        :disabled="currentPage === 1"
        class="btn-prev mx-2 rounded bg-gray-300 px-4 py-2 text-gray-700 disabled:opacity-50">
        Anterior
      </button>
      <span>Página {{ currentPage }} de {{ totalPages }}</span>
      <button
        @click="nextPage"
        :disabled="currentPage === totalPages"
        class="btn-next mx-2 rounded bg-gray-300 px-4 py-2 text-gray-700 disabled:opacity-50">
        Próxima
      </button>
    </div>

    <!-- Modal para ver mais detalhes -->
    <Modal v-if="showModal" @close="showModal = false">
      <template #header>
        <h3 class="text-xl font-bold">{{ modalData.OBJECT_NAME }} - Detalhes completos</h3>
      </template>
      <template #body>
        <p>
          <strong>Object ID:</strong>
          {{ modalData.OBJECT_ID }}
        </p>
        <p>
          <strong>Eccentricity:</strong>
          {{ modalData.ECCENTRICITY }}
        </p>
        <p>
          <strong>Inclination:</strong>
          {{ modalData.INCLINATION }}°
        </p>
        <p>
          <strong>Arg of Pericenter:</strong>
          {{ modalData.ARG_OF_PERICENTER }}
        </p>
        <p>
          <strong>Mean Motion:</strong>
          {{ modalData.MEAN_MOTION }}
        </p>
        <p>
          <strong>RA of Asc Node:</strong>
          {{ modalData.RA_OF_ASC_NODE }}
        </p>
        <p>
          <strong>Mean Anomaly:</strong>
          {{ modalData.MEAN_ANOMALY }}
        </p>
        <p>
          <strong>Ephemeris Type:</strong>
          {{ modalData.EPHEMERIS_TYPE }}
        </p>
        <p>
          <strong>NORAD Cat ID:</strong>
          {{ modalData.NORAD_CAT_ID }}
        </p>
        <!-- Adicionar mais campos conforme necessário -->
      </template>
      <template #footer>
        <button
          @click="showModal = false"
          class="mt-4 rounded-lg bg-gray-500 px-4 py-2 font-bold text-white hover:bg-gray-700">
          Fechar
        </button>
      </template>
    </Modal>
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
    filteredData() {
      if (!this.searchQuery) {
        return this.data
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
    openModal(row) {
      this.modalData = row
      this.showModal = true
    }
  }
}
</script>

<!-- Tailwind CSS aplicado -->
<style scoped>
.table-container {
  @apply flex flex-col;
}
.card {
  @apply rounded-lg border border-gray-300 bg-gray-100 p-6 shadow-lg;
}
.pagination button {
  @apply rounded-lg bg-gray-300 px-4 py-2 text-gray-700 disabled:opacity-50;
}
.search-container {
  @apply my-4 flex items-center justify-center;
}
</style>
