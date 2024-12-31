<template>
  <div class="mb-10 px-6">
    <div class="text-white">
      <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Ground Track</div>
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
            <section class="rounded-lg bg-white p-6">
              <h2 class="mb-4 text-lg font-semibold">O que é Ground Track?</h2>
              <p class="mb-4 text-base leading-relaxed">
                O
                <span class="font-semibold">ground track</span>
                , ou trajetória no solo, é a projeção do movimento de um satélite em órbita na superfície terrestre. Ele
                representa a posição do satélite em relação à Terra ao longo do tempo, como se fosse uma "sombra" do
                satélite movendo-se sobre o planeta.
              </p>

              <h3 class="mb-2 text-lg font-medium">Características Principais</h3>
              <ul class="mb-4 list-disc pl-6">
                <li>
                  O formato do ground track depende do tipo de órbita do satélite (ex.: polar, geoestacionária,
                  elíptica).
                </li>
                <li>
                  Em órbitas baixas, ele frequentemente aparece como uma série de curvas sinuosas devido à rotação da
                  Terra.
                </li>
                <li>
                  Satélites geoestacionários têm um ground track fixo, pois permanecem acima do mesmo ponto na
                  superfície.
                </li>
              </ul>

              <h3 class="mb-2 text-lg font-medium">Importância do Ground Track</h3>
              <p class="text-base leading-relaxed">
                O estudo do ground track é fundamental em diversas aplicações, como:
              </p>
              <ol class="mb-4 list-decimal pl-6">
                <li>Planejamento de missões de observação da Terra.</li>
                <li>Posicionamento de antenas para comunicação via satélite.</li>
                <li>Previsão de passagens de satélites visíveis a olho nu.</li>
              </ol>
            </section>

            <section class="rounded-lg p-6">
              <h2 class="mb-4 text-lg font-semibold">Curiosidade</h2>
              <p class="text-base leading-relaxed">
                Um ground track pode ser visualizado em softwares de simulação orbital ou ferramentas online, permitindo
                entender melhor como satélites se movem em relação à superfície terrestre. Essas projeções ajudam a
                otimizar trajetórias e a prever eventos como eclipses.
              </p>
            </section>
          </div>
        </div>
      </transition>
    </div>

    <!-- Aplicação -->
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
import LineChart from '@/modules/LineChartGT.vue'

export default {
  name: 'GroundTrack',
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
            },
            min: -180,
            max: 180
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
            },
            min: -90,
            max: 90
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
  computed: {},
  mounted() {
    this.updateOrientation() // Atualizar orientação no início
    window.addEventListener('resize', this.updateOrientation)
  },
  methods: {
    updateOrientation() {
      this.isLandscape = window.matchMedia('(orientation: landscape)').matches
    },
    toggle() {
      this.isOpen = !this.isOpen
    }
  }
}
</script>
