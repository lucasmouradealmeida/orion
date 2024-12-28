<template>
  <div class="mb-10 px-6">
    <div class="text-white">
      <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Pontos de Lagrange</div>
    </div>

    <!-- Teoria -->
    <div class="group px-6">
      <div class="flex cursor-pointer items-center justify-between space-x-2 rounded" @click="toggle">
        <h2 class="text-medium w-max font-semibold text-white">Teoria</h2>

        <span
          class="flex shrink-0 cursor-pointer items-center rounded-lg transition-transform duration-300"
          :class="{ '-rotate-180': isOpen }">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="size-5 h-6 w-6 text-white"
            viewBox="0 0 20 20"
            fill="currentColor">
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd" />
          </svg>
        </span>

        <!-- Linha horizontal -->
        <div class="mt-2 h-[1px] w-full bg-white"></div>
      </div>

      <!-- Conteúdo da seção expansível com transição -->
      <transition name="fade">
        <div v-if="isOpen" class="content mt-2 rounded-xl border border-gray-200 bg-white p-4">
          <div class="bg-gray-50 p-6 text-justify">
            <div class="rounded-lg bg-white">
              <p class="mb-4 text-base text-gray-700">
                Os
                <strong class="font-bold text-gray-900">pontos de equilíbrio de Lagrange</strong>
                são pontos específicos no espaço onde a força gravitacional de dois corpos principais se equilibra com a
                força centrífuga experimentada por um objeto que se move com eles. Esses pontos são importantes em
                mecânica celeste e astrodinâmica e são usados para posicionar satélites e sondas espaciais.
              </p>

              <h2 class="mb-4 mt-6 text-xl font-semibold text-gray-800">Características dos Pontos Lagrangeanos</h2>
              <p class="mb-4 text-base text-gray-700">
                Existem cinco pontos de Lagrange, numerados de
                <strong class="font-bold text-gray-900">L1 a L5</strong>
                , e eles têm diferentes características de estabilidade e de velocidade:
              </p>

              <div class="space-y-6">
                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L1 - Ponto de Equilíbrio Instável</h3>
                  <p class="text-md text-gray-700">
                    Localizado entre os dois corpos (como a Terra e o Sol), o ponto L1 é o mais utilizado para missões
                    espaciais. Um objeto neste ponto tem a velocidade orbital igual à dos corpos principais e permanece
                    "parado" em relação ao sistema de referência. No entanto, o ponto L1 é instável, ou seja, pequenas
                    perturbações podem fazer com que o objeto se desvie. A curva de velocidade zero neste ponto define a
                    linha de equilíbrio de velocidade.
                  </p>
                </div>

                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L2 - Ponto de Equilíbrio Instável</h3>
                  <p class="text-base text-gray-700">
                    Localizado do lado oposto ao L1, fora da órbita dos corpos principais. Embora o objeto também tenha
                    velocidade zero neste ponto, o L2 é instável e, assim como o L1, pequenas alterações podem desviar o
                    objeto.
                  </p>
                </div>

                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L3 - Ponto de Equilíbrio Instável</h3>
                  <p class="text-base text-gray-700">
                    Fica do lado oposto ao ponto L1, na direção da órbita dos corpos principais. Este ponto é instável e
                    não seria utilizado para posicionamento de objetos de forma estável.
                  </p>
                </div>

                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L4 e L5 - Pontos de Equilíbrio Estáveis</h3>
                  <p class="text-base text-gray-700">
                    Estes pontos estão localizados ao longo da órbita dos corpos principais, formando um triângulo
                    equilátero com os corpos. Objetos nestes pontos podem ter uma velocidade zero em relação ao sistema
                    de referência e, devido à sua estabilidade, não precisam de ajustes contínuos para permanecer no
                    ponto.
                  </p>
                </div>
              </div>

              <h2 class="mb-4 mt-6 text-2xl font-semibold text-gray-800">Curvas de Velocidade Zero</h2>
              <p class="mb-4 text-base text-gray-700">
                A curva de velocidade zero descreve as regiões onde a velocidade do objeto é zero no referencial
                rotativo dos dois corpos. Em outras palavras, é a condição em que o objeto pode ficar parado em relação
                ao sistema de referência sem precisar de velocidade adicional para se manter ali.
              </p>

              <div class="mt-6">
                <h3 class="mb-2 text-xl font-semibold text-gray-800">Resumo das Curvas de Velocidade Zero</h3>
                <ul class="list-disc space-y-2 pl-5 text-base text-gray-700">
                  <li>
                    <strong>L1 e L2:</strong>
                    Curvas de velocidade zero instáveis, onde pequenas perturbações podem fazer com que o objeto se
                    desvie.
                  </li>
                  <li>
                    <strong>L4 e L5:</strong>
                    Curvas de velocidade zero estáveis, onde objetos podem permanecer em repouso relativo sem a
                    necessidade de ajustes contínuos.
                  </li>
                </ul>
              </div>

              <div class="text-red-500 mt-6 text-sm">
                <p>
                  <strong>Nota:</strong>
                  Para L1 e L2, embora o ponto possa ser utilizado para posicionamento, é necessário um sistema de
                  controle para garantir a estabilidade, já que esses pontos são instáveis. Já L4 e L5 são preferíveis
                  para estabilidade a longo prazo.
                </p>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>

    <!-- Aplicação -->
    <div
      class="mt-6 flex flex-col items-center space-y-4 px-6 md:flex-row md:space-x-4 md:space-y-0 lg:flex-row lg:space-x-4 lg:space-y-0">
      <!-- Primeiro Select -->
      <div class="flex items-center space-x-2">
        <label for="body1" class="text-white">Primeiro corpo celeste:</label>
        <select id="body1" class="rounded-lg p-2" v-model="selectedBody1" @change="updateBody2Options">
          <option v-for="body in celestialBodies" :key="body" :value="body.value">
            {{ body.name }}
          </option>
        </select>
      </div>

      <!-- Segundo Select -->
      <div class="flex items-center space-x-2">
        <label for="body2" class="text-white">Segundo corpo celeste:</label>
        <select id="body2" class="rounded-lg p-2" v-model="selectedBody2">
          <option v-for="body in filteredBodies" :key="body" :value="body.value">
            {{ body.name }}
          </option>
        </select>
      </div>

      <!-- Determinar os pontos de curva de velocidade zero -->
      <div class="flex items-center">
        <button class="rounded-lg bg-[#324AB2] p-2 text-white" @click="calculateLagrangePoints">Calcular</button>
      </div>
    </div>
  </div>

  <div v-if="!isLandscape" class="flex h-[40vh] items-center justify-center text-white">
    <div class="flex w-[50vw] flex-col items-center">
      <p class="text-justify">Gire o dispositivo para visualizar o gráfico.</p>
      <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="mt-2 h-10 w-10" viewBox="0 0 16 16">
        <path
          d="M1 4.5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm-1 6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2z" />
        <path d="M14 7.5a1 1 0 1 0-2 0 1 1 0 0 0 2 0" />
      </svg>
    </div>
  </div>
  <div v-else>
    <LineChart :chart-data="graphData" :options="graphOptions" class="p-6" ref="pageChart"></LineChart>
  </div>
  <!-- Alerta -->
  <Alert ref="alertComponent" />
</template>

<script>
import Alert from '@/components/Alert.vue'
import LineChart from '@/modules/LineChart.vue'

export default {
  name: 'PontosLagrange',
  components: {
    Alert,
    LineChart
  },
  data() {
    return {
      isLandscape: window.matchMedia('(orientation: landscape)').matches,
      isOpen: false,
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
      },
      // Lista de corpos celestes
      celestialBodies: [
        { value: 'sun', name: 'Sol', mass: 1989000e24 },
        { value: 'mercury', name: 'Mercúrio', mass: 0.33e24 },
        { value: 'venus', name: 'Vênus', mass: 4.87e24 },
        { value: 'earth', name: 'Terra', mass: 5.97e24 },
        { value: 'mars', name: 'Marte', mass: 0.642e24 },
        { value: 'jupiter', name: 'Júpiter', mass: 1898e24 },
        { value: 'saturn', name: 'Saturno', mass: 568e24 },
        { value: 'uranus', name: 'Urano', mass: 86.8e24 },
        { value: 'neptune', name: 'Netuno', mass: 102e24 }
      ],
      selectedBody1: null, // Corpo selecionado no primeiro select
      selectedBody2: null // Corpo selecionado no segundo select
    }
  },
  computed: {
    // Corpos celestes disponíveis para o segundo select
    filteredBodies() {
      return this.celestialBodies.filter((body) => body.value !== this.selectedBody1)
    }
  },
  mounted() {
    this.updateOrientation() // Atualizar orientação no início
    window.addEventListener('resize', this.updateOrientation)
  },
  methods: {
    updateOrientation() {
      this.isLandscape = window.matchMedia('(orientation: landscape)').matches
    },
    // Atualiza a seleção no segundo select quando o primeiro muda
    updateBody2Options() {
      if (this.selectedBody2 === this.selectedBody1) {
        this.selectedBody2 = null
      }
    },
    toggle() {
      this.isOpen = !this.isOpen
    },
    async calculateLagrangePoints() {
      // Verifica se os corpos forma selecionados
      if (this.selectedBody1 && this.selectedBody2) {
        // Cálculos dos pontos de Lagrange
        const rawResponse = await fetch('/lagrange/points', {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
          },
          body: JSON.stringify({
            corpo1: this.selectedBody1,
            corpo2: this.selectedBody2,
            massa1: this.celestialBodies.find((body) => body.value === this.selectedBody1).mass,
            massa2: this.celestialBodies.find((body) => body.value === this.selectedBody2).mass
          })
        })

        const content = await rawResponse.json()

        // Pontos de Lagrange
        for (let i = 0; i < content['L'].length; i++) {
          this.graphData.datasets.push({
            label: `L${i + 1}`,
            data: [{ x: content['L'][i][0], y: content['L'][i][1] }],
            showLine: false,
            pointRadius: 5
          })
        }

        // Ponto dos corpos celestes
        this.graphData.datasets.push({
          label: content['corpo_maior'],
          data: [{ x: 0, y: 0 }],
          showLine: false,
          pointRadius: 5
        })

        this.graphData.datasets.push({
          label: content['corpo_menor'],
          data: [{ x: content['distancia'], y: 0 }],
          showLine: false,
          pointRadius: 5
        })

        // Curvas de velocidade zero
        let dados = []

        for (let i = 0; i < content['par_ordenado'].length; i++) {
          let pontos = content['par_ordenado'][i]['pontos']
          for (let j = 0; j < pontos.length; j++) {
            dados.push({ x: pontos[j][0], y: pontos[j][1] })
          }

          let newDataset = {
            label: `Cj = ${content['par_ordenado'][i]['Cj']}`, // Adiciona rótulo para identificação
            data: dados,
            borderWidth: 1,
            showLine: false, // Garante que não há linhas conectando os pontos
            pointRadius: 0.5, // Tamanho dos pontos (opcional)
            pointBackgroundColor: 'rgba(75, 192, 192, 1)' // Cor dos pontos (opcional)
          }

          this.graphData.datasets.push(newDataset)
          dados = []
        }

        const pageChart = this.$refs.pageChart
        pageChart.update()
      } else {
        this.$refs.alertComponent.triggerAlert('warning', 'Necessário selecionar dois corpos celestes', 5000)
      }
    }
  }
}
</script>

<style scoped>
/* Transição personalizada */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
