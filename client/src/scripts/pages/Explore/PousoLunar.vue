<template>
  <div class="px-6">
    <div class="text-white">
      <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Pouso Lunar</div>
    </div>

    <div class="ml-4 mr-4 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="button in buttons"
        :key="button.id"
        @click="executeAction(button.action, true)"
        class="group relative inline-flex cursor-pointer items-center overflow-hidden rounded bg-[#324ab2] px-8 py-3 text-white focus:outline-none focus:ring active:bg-[#324ab2]">
        <span class="absolute -end-full transition-all group-hover:end-4">
          <svg
            class="h-[20px] w-[20px] rtl:rotate-180"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="0 0 24 24"
            stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
          </svg>
        </span>

        <span class="text-sm font-medium transition-all group-hover:me-4">{{ button.label }}</span>
      </div>
    </div>

    <LineChart :chart-data="graphData" :options="graphOptions" class="p-6" ref="pageChart"></LineChart>
  </div>

  <Modal v-if="modalPousoSuave" v-model="modalPousoSuave" @close="modalPousoSuave = false">
    <template v-slot:header>
      <h2 class="text-lg font-bold">Pouso suave</h2>
    </template>

    <template v-slot:body>
      <div class="grid grid-cols-2 gap-4 p-6">
        <div class="flex flex-col space-y-2">
          <label for="ps_massa" class="text-sm font-medium">Massa</label>
          <input id="ps_massa" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_gravidade" class="text-sm font-medium">Gravidade</label>
          <input id="ps_gravidade" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_intensidade" class="text-sm font-medium">Intensidade</label>
          <input id="ps_intensidade" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_angulo" class="text-sm font-medium">Ângulo</label>
          <input id="ps_angulo" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_altura" class="text-sm font-medium">Altura</label>
          <input id="ps_altura" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_velocidade" class="text-sm font-medium">Velocidade</label>
          <input id="ps_velocidade" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_curva_cor" class="text-sm font-medium">Cor da curva</label>
          <input id="ps_curva_cor" type="color" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="ps_label" class="text-sm font-medium">Nome</label>
          <input id="ps_label" type="text" class="input" />
        </div>
      </div>
    </template>

    <template v-slot:footer>
      <div class="flex w-full flex-row justify-center space-x-4 p-6">
        <button
          @click="executeAction('modalPousoSuave', false)"
          class="inline-block rounded border border-[#b23237] px-12 py-3 text-sm font-medium text-[#b23237] hover:bg-[#b23237] hover:text-white focus:outline-none focus:ring active:bg-[#b23237]">
          Cancelar
        </button>

        <button
          @click="curvaPousoSuave(), executeAction('modalPousoSuave', false)"
          class="inline-block rounded border border-[#45b232] px-12 py-3 text-sm font-medium text-[#45b232] hover:bg-[#45b232] hover:text-white focus:outline-none focus:ring active:bg-[#45b232]">
          Salvar
        </button>
      </div>
    </template>
  </Modal>

  <Modal v-if="modalCurvaVelocidade" v-model="modalCurvaVelocidade" @close="modalCurvaVelocidade = false">
    <template v-slot:header>
      <h2 class="text-lg font-bold">Curva de velocidade</h2>
    </template>

    <template v-slot:body>
      <div class="grid grid-cols-2 gap-4 p-6">
        <div class="flex flex-col space-y-2">
          <label for="cv_massa" class="text-sm font-medium">Massa</label>
          <input id="cv_massa" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_gravidade" class="text-sm font-medium">Gravidade</label>
          <input id="cv_gravidade" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_intensidade" class="text-sm font-medium">Intensidade</label>
          <input id="cv_intensidade" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_angulo" class="text-sm font-medium">Ângulo</label>
          <input id="cv_angulo" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_altura_inicial" class="text-sm font-medium">Altura inicial</label>
          <input id="cv_altura_inicial" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_velocidade_inicial" class="text-sm font-medium">Velocidade inicial</label>
          <input id="cv_velocidade_inicial" type="number" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_curva_cor" class="text-sm font-medium">Cor da curva</label>
          <input id="cv_curva_cor" type="color" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_point_cor" class="text-sm font-medium">Cor do ponto</label>
          <input id="cv_point_cor" type="color" class="input" />
        </div>

        <div class="flex flex-col space-y-2">
          <label for="cv_label" class="text-sm font-medium">Nome</label>
          <input id="cv_label" type="text" class="input" />
        </div>
      </div>
    </template>

    <template v-slot:footer>
      <div class="flex w-full flex-row justify-center space-x-4 p-6">
        <button
          @click="executeAction('modalCurvaVelocidade', false)"
          class="inline-block rounded border border-[#b23237] px-12 py-3 text-sm font-medium text-[#b23237] hover:bg-[#b23237] hover:text-white focus:outline-none focus:ring active:bg-[#b23237]">
          Cancelar
        </button>

        <button
          @click="curvaVelocidade(), executeAction('modalCurvaVelocidade', false)"
          class="inline-block rounded border border-[#45b232] px-12 py-3 text-sm font-medium text-[#45b232] hover:bg-[#45b232] hover:text-white focus:outline-none focus:ring active:bg-[#45b232]">
          Salvar
        </button>
      </div>
    </template>
  </Modal>

  <Modal v-if="modalDeleteCurves" v-model="modalDeleteCurves" @close="modalDeleteCurves = false">
    <template v-slot:header>
      <h2 class="text-lg font-bold">Tem certeza que deseja deletar os dados?</h2>
    </template>
    <template v-slot:footer>
      <div class="flex w-full flex-row justify-center space-x-4 p-6">
        <button
          @click="executeAction('modalDeleteCurves', false)"
          class="inline-block rounded border border-[#45b232] px-12 py-3 text-sm font-medium text-[#45b232] hover:bg-[#45b232] hover:text-white focus:outline-none focus:ring active:bg-[#45b232]">
          Cancelar
        </button>

        <button
          @click="deleteCurves(), executeAction('modalDeleteCurves', false)"
          class="inline-block rounded border border-[#b23237] px-12 py-3 text-sm font-medium text-[#b23237] hover:bg-[#b23237] hover:text-white focus:outline-none focus:ring active:bg-[#b23237]">
          Deletar
        </button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from '@/components/Modal'
import LineChart from '@/modules/LineChart.vue'

export default {
  name: 'PousoLunar',
  components: {
    Modal,
    LineChart
  },
  data() {
    return {
      modalRangeX: false,
      modalRangeY: false,
      modalPousoSuave: false,
      modalCurvaVelocidade: false,
      modalDeleteCurves: false,
      buttons: [
        {
          id: 1,
          label: 'Pouso suave',
          action: 'modalPousoSuave'
        },
        {
          id: 2,
          label: 'Curva de velocidade',
          action: 'modalCurvaVelocidade'
        },
        {
          id: 3,
          label: 'Apagar curvas',
          action: 'modalDeleteCurves'
        }
      ],
      graphData: {
        datasets: []
      },
      graphOptions: {
        maintainAspectRatio: false,
        tension: 0.4,
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Velocidade Vertical',
              font: {
                size: 14,
                weight: 'bolder'
              }
            },
            type: 'linear',
            ticks: {
              font: {
                size: 14,
                weight: 'bolder'
              }
            }
          },
          y: {
            beginAtZero: true,
            display: true,
            title: {
              display: true,
              text: 'Altitude',
              font: {
                size: 14,
                weight: 'bolder'
              }
            },
            type: 'linear',
            ticks: {
              font: {
                size: 14,
                weight: 'bolder'
              }
            }
          }
        },
        elements: {
          point: {
            radius: 0 // Define o raio do ponto como 0 para não exibir pontos
          }
        },
        plugins: {
          legend: {
            display: true
          }
        }
      }
    }
  },
  methods: {
    deleteCurves() {
      this.graphData.datasets = []
      const pageChart = this.$refs.pageChart
      pageChart.update()
    },

    executeAction(action, flag) {
      this[action] = flag
      if (flag) {
        document.querySelector('body').style.overflow = 'hidden'
      } else {
        document.querySelector('body').style.overflow = 'auto'
      }
    },

    async curvaVelocidade() {
      const y = parseInt(document.getElementById('cv_altura_inicial').value)
      const x = parseInt(document.getElementById('cv_velocidade_inicial').value)
      const corCurva = document.getElementById('cv_curva_cor').value
      const corPonto = document.getElementById('cv_point_cor').value
      const nome = document.getElementById('cv_label').value
      const massa = parseFloat(document.getElementById('cv_massa').value)
      const gravidade = parseFloat(document.getElementById('cv_gravidade').value)
      const intensidade = parseFloat(document.getElementById('cv_intensidade').value)
      const angulacao = parseFloat(document.getElementById('cv_angulo').value)

      const rawResponse = await fetch('/pouso/curva/velocidade', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
        },
        body: JSON.stringify({
          massa: massa,
          gravidade: gravidade,
          intensidade: intensidade,
          angulacao: angulacao,
          altura: y,
          velocidade_inicial: x
        })
      })

      const content = await rawResponse.json()
      this.addCurvaVelocidade(content.velocidade, content.altura, corCurva, nome, corPonto, x, y)
    },

    async curvaPousoSuave() {
      const corCurva = document.getElementById('ps_curva_cor').value
      const nome = document.getElementById('ps_label').value
      const altura = parseInt(document.getElementById('ps_altura').value)
      const velocidade = parseInt(document.getElementById('ps_velocidade').value)
      const massa = parseFloat(document.getElementById('ps_massa').value)
      const gravidade = parseFloat(document.getElementById('ps_gravidade').value)
      const intensidade = parseFloat(document.getElementById('ps_intensidade').value)
      const angulacao = parseFloat(document.getElementById('ps_angulo').value)

      const rawResponse = await fetch('/pouso/curva/pouso/suave', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
        },
        body: JSON.stringify({
          massa: massa,
          gravidade: gravidade,
          intensidade: intensidade,
          angulacao: angulacao,
          altura: altura,
          velocidade: velocidade
        })
      })

      const content = await rawResponse.json()
      console.log(content)
      this.addCurvaVelocidade(content.velocidade, content.altura, corCurva, nome, null, null, null)
    },

    addCurvaVelocidade(velocidade, altura, corCurva, nome, corPonto, x, y) {
      let dados = []

      // Monta os objetos {x, y} para cada par de valores
      for (let i = 0; i < velocidade.length; i++) {
        dados.push({ x: velocidade[i], y: altura[i] })
      }

      const newDataset = {
        label: nome,
        data: dados,
        borderColor: corCurva,
        backgroundColor: 'transparent',
        borderWidth: 1
      }

      this.graphData.datasets.push(newDataset)

      // Criar um novo conjunto de dados com o ponto adicionado
      if (corPonto && x && y) {
        const newPoint = {
          label: 'Ponto: ' + nome,
          data: [{ x: x, y: y }],
          showLine: false,
          pointRadius: 5,
          pointBackgroundColor: corPonto,
          borderColor: corPonto,
          backgroundColor: corPonto
        }

        this.graphData.datasets.push(newPoint)
      }

      const pageChart = this.$refs.pageChart
      pageChart.update()
    },

    addPointToDataset() {
      const y = parseFloat(document.getElementById('cv_altura_inicial').value)
      const x = parseFloat(document.getElementById('cv_velocidade_inicial').value)
      const cor = document.getElementById('cv_point_cor').value
      const nome = document.getElementById('cv_label').value

      // Encontrar o índice correspondente ao valor x no array de labels
      const index = this.graphData.labels.reduce((prevIndex, label, i) => {
        const labelValue = parseFloat(label)
        const prevLabelValue = parseFloat(this.data.labels[prevIndex])
        const xValue = parseFloat(x.toFixed(1))

        const diff = Math.abs(labelValue - xValue)
        const prevDiff = Math.abs(prevLabelValue - xValue)

        return diff < prevDiff ? i : prevIndex
      }, 0)

      // Criar um novo conjunto de dados com o ponto adicionado
      const newDataset = {
        label: nome,
        data: this.data.labels.map((label, i) => (i === index ? y : null)),
        showLine: false,
        pointRadius: 5,
        pointBackgroundColor: cor,
        borderColor: cor,
        backgroundColor: cor
      }

      // Adicionar o novo conjunto de dados ao array de datasets
      this.graphData.datasets.push(newDataset)
      // Atualizar o gráfico
      const pageChart = this.$refs.pageChart
      pageChart.update()
    }
  }
}
</script>
