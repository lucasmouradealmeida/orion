<template>
  <div class="px-6">
    <div class="text-white">
      <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Two Lines</div>
    </div>

    <div class="mb-9 ml-4 mt-4 flex flex-col space-y-6 lg:flex-row lg:space-x-6 lg:space-y-0">
      <div>
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

    <TableCards :data="celestrakObjects" :itemsPerPage="6" :loading="loadingCelestrak" />
  </div>
</template>

<script>
import { ref } from 'vue'
import TableCards from '@/modules/TableCards.vue'

export default {
  name: 'Twolines',
  components: {
    TableCards
  },
  data() {
    return {
      loadingCelestrak: false,
      celestrackGroups: window.__site__.context.groups[0],
      celestrakObjects: [],
      selectSatelite: document.querySelector('#satelite')
    }
  },
  mounted() {
    this.selectSatelite = document.querySelector('#satelite')
  },
  methods: {
    async findSatelites(code) {
      this.loadingCelestrak = true

      const rawResponse = await fetch(
        `https://celestrak.org/NORAD/elements/gp.php?GROUP=${code}&FORMAT=json-pretty`,
        {}
      )

      const content = await rawResponse.json()
      this.loadingCelestrak = false
      this.celestrakObjects = content
      this.rowData = ref(content)
    }
  }
}
</script>
