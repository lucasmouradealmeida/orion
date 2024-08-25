<template>
  <div class="text-white">
    <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Two Lines</div>
  </div>

  <div class="ml-4 mt-4 flex flex-col space-y-6 lg:flex-row lg:space-x-6 lg:space-y-0">
    <div>
      <div for="celestrakGroups" class="text-md mb-2 block font-medium text-white">Agrupamentos de Satélites</div>
      <select
        @input="findSatelites($event.target.value)"
        name="celestrakGroups"
        id="celestrakGroups"
        class="mt-1.5 cursor-pointer rounded-lg border-gray-300 p-2 font-medium text-black sm:text-sm">
        <option value="" selected hidden>Selecione um agrupamento</option>
        <option v-for="group in celestrackGroups" :value="group.code">{{ group.name }}</option>
      </select>
    </div>
  </div>

  <div class="p-10 pl-4">
    <div class="text-md mb-2 block font-medium text-white">Dados</div>
    <input
      type="text"
      @input="onFilterTextChanged"
      placeholder="Filtrar tabela"
      class="mb-4 rounded-lg border-gray-300 p-2 font-medium text-black sm:text-sm" />
    <ag-grid-vue
      :rowData="rowData"
      :loading="rowData"
      :overlayNoRowsTemplate="'Nenhum dado encontrado'"
      :columnDefs="colDefs"
      :pagination="true"
      :paginationPageSize="5"
      paginationAutoPageSize="true"
      style="width: 100%; height: 340px"
      :defaultColDef="defaultColDef"
      class="ag-theme-quartz"></ag-grid-vue>
  </div>
</template>

<script>
import { ref } from 'vue'
import 'ag-grid-community/styles/ag-grid.css'
import 'ag-grid-community/styles/ag-theme-quartz.css'
import { AgGridVue } from 'ag-grid-vue3'

export default {
  name: 'Twolines',
  components: {
    AgGridVue
  },
  data() {
    return {
      celestrackGroups: window.__site__.context.groups[0],
      celestrakObjects: null,
      selectSatelite: document.querySelector('#satelite'),
      defaultColDef: {
        flex: 1,
        filter: true,
        filterParams: {
          buttons: ['reset', 'apply'],
          closeOnApply: true
        }
      },
      colDefs: ref([
        { field: 'ARG_OF_PERICENTER', headerName: 'Argumento do Pericentro', resizable: false, minWidth: 250 },
        { field: 'BSTAR', resizable: false, headerName: 'Bstar', minWidth: 120 },
        { field: 'CLASSIFICATION_TYPE', resizable: false, headerName: 'Tipo de classificação', minWidth: 200 },
        { field: 'ECCENTRICITY', resizable: false, headerName: 'Excentricidade', minWidth: 150 },
        { field: 'ELEMENT_SET_NO', resizable: false, headerName: 'Número do elemento', minWidth: 200 },
        { field: 'EPHEMERIS_TYPE', resizable: false, headerName: 'Tipo de efeméride', minWidth: 180 },
        { field: 'EPOCH', resizable: false, headerName: 'Epoch', minWidth: 150 },
        { field: 'INCLINATION', resizable: false, headerName: 'Inclinação', minWidth: 150 },
        { field: 'MEAN_ANOMALY', resizable: false, headerName: 'Anomalia média', minWidth: 180 },
        { field: 'MEAN_MOTION', resizable: false, headerName: 'Movimento médio', minWidth: 180 },
        { field: 'MEAN_MOTION_DDOT', resizable: false, headerName: 'Mudança de movimento médio', minWidth: 250 },
        { field: 'MEAN_MOTION_DOT', resizable: false, headerName: 'Ponto de movimento médio', minWidth: 250 },
        { field: 'NORAD_CAT_ID', resizable: false, headerName: 'ID NORAD', minWidth: 150 },
        { field: 'OBJECT_ID', resizable: false, headerName: 'ID do objeto', minWidth: 150 },
        { field: 'OBJECT_NAME', resizable: false, headerName: 'Nome do objeto', minWidth: 180 },
        { field: 'RA_OF_ASC_NODE', resizable: false, headerName: 'RA do nó ascendente', minWidth: 200 },
        { field: 'REV_AT_EPOCH', resizable: false, headerName: 'Revolução na época', minWidth: 200 }
      ]),
      rowData: null
    }
  },
  mounted() {
    this.selectSatelite = document.querySelector('#satelite')
  },
  methods: {
    async findSatelites(code) {
      const rawResponse = await fetch(
        `https://celestrak.org/NORAD/elements/gp.php?GROUP=${code}&FORMAT=json-pretty`,
        {}
      )

      const content = await rawResponse.json()
      this.celestrakObjects = content
      this.rowData = ref(content)
    },
    onFilterTextChanged() {
      if (!this.celestrakObjects) {
        return
      }
      const data = this.celestrakObjects
      const filterText = document.querySelector('input').value
      if (!filterText) {
        this.rowData = ref(this.celestrakObjects)
        return
      }
      const filteredData = data.filter((item) => {
        return Object.keys(item).some((key) => {
          return String(item[key]).toLowerCase().includes(filterText.toLowerCase())
        })
      })
      this.rowData = ref(filteredData)
    }
  }
}
</script>
