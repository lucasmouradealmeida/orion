<template>
  <div class="main">
    <div class="content">
      <div v-show="home" class="content-home">
        <div class="container">
          <div class="title">Sobre</div>
          <div class="divider"></div>

          <div class="paragraph text-justify indent-12">
            Este projeto tem como intuito passar alguns dos conhecimentos aprendidos ao longo da graduação em Engenheira
            Aeroespacial. Campo que incorpora o estado da arte da engenharia aplicada ao projeto, análise, construção e
            testes de sistemas associados com o Setor Aeroespacial, envolvendo aeronaves, foguetes e satélites
            artificiais. Seus conhecimentos incluem sistemas de propulsão, comunicação, controle de aeronaves, navegação
            e interação homem-máquina. As tecnologias que este profissional utilizará são complementadas com noções de
            sensores e instrumentação de bordo, de materiais especiais, de aerodinâmica e de controle de temperatura. A
            formação na UFABC possibilita amplos conhecimentos de física, química, matemática, computação e noções
            fundamentais de engenharia.
          </div>

          <div class="title">Perfil do profissional</div>
          <div class="divider"></div>

          <div class="paragraph text-justify indent-12">
            É o engenheiro apto a atuar em modelagem, controle, projeto, análise, construção e testes de sistemas no
            setor aeroespacial Atuação: Pesquisa científica nas várias entidades que estudam aeronaves e veículos
            espaciais no Brasil (UFABC, INPE, CTA, AEB,...) Indústria: qualquer empresa que presta serviço ao setor
            aeroespacial (EMBRAER, AVIBRAS, Helibrás, etc). Empresário autônomo como fabricante/fornecedor de peças,
            componentes, serviços e soluções para o mercado aeroespacial brasileiro.
          </div>

          <div class="title">Atuação profissional</div>
          <div class="divider"></div>

          <div class="paragraph text-justify indent-12">
            Desenvolvimento e a avaliação de sistemas diversos (computação, eletrônicos, mecânicos, hidráulicos)
            associados a aeronaves, foguetes e sondas espaciais. Desenvolvimento de satélites artificiais (modelagem,
            controle,...) para diversas finalidades (satélites meteorológicos, de comunicação, observacionais) Sistemas
            de propulsão, comunicação, controle de atitude, navegação, interação homem-máquina,... Sensores e
            instrumentação de bordo, materiais especiais, aerodinâmica, controle de temperatura, controle de vibração,
            em sistemas diversos associados a aeronaves, foguetes,...
          </div>

          <div class="title">Formação na UFABC</div>
          <div class="divider"></div>

          <div class="paragraph text-justify indent-12">
            Para a sua formação como Engenheiro Espacial, nosso curso oferece as seguintes disciplinas: Aerodinâmica,
            Aeroelasticidade, Astrodinâmica, Aviônica, Ciência dos Materiais, Controle de aeronaves, Desempenho, Ensaios
            em vôo, Estabilidade de vôo, Helicópteros, Instrumentação e sistemas, Propulsão, Sistemas de radar. Ao longo
            do curso, também serão estudados: Circuitos elétricos, Estruturas, Gestão, Matemática, Mecânica clássica,
            Mecânica dos Ruídos, Mecânica dos sólidos, Probabilidades e Estatística, Telecomunicações, Termodinâmica e
            Vibrações e ruído.
          </div>
        </div>
      </div>

      <div v-show="explore" class="content-explore">
        <div class="pagetitle">
          <div class="title">Explore</div>
        </div>

        <div class="cards">
          <div class="card cursor-pointer" @click="(pousoLunar = true), (explore = false)">
            <div class="cardback"></div>
            <svg
              @click="(pousoLunar = true), (explore = false)"
              class="expandcard h-6 w-6 text-white"
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
                d="m9 5 7 7-7 7" />
            </svg>
            <div class="cardcontent">
              <div>Pouso Lunar</div>
            </div>
          </div>

          <div class="card cursor-pointer" @click="(twolines = true), (explore = false)">
            <div class="cardback"></div>
            <svg
              @click="(twolines = true), (explore = false)"
              class="expandcard h-6 w-6 text-white"
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
                d="m9 5 7 7-7 7" />
            </svg>
            <div class="cardcontent">
              <div>Two Lines</div>
            </div>
          </div>
        </div>
      </div>

      <div v-show="pousoLunar">
        <div class="ml-6 mt-10 flex flex-row">
          <div class="ml-6 mr-6 cursor-pointer content-center">
            <svg
              @click="(pousoLunar = false), (explore = true)"
              class="h-6 w-6 scale-125 text-gray-800 dark:text-white"
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
                d="m15 19-7-7 7-7" />
            </svg>
          </div>
          <div class="w-fit content-center text-3xl font-bold text-white">Pouso Lunar</div>
        </div>

        <div class="mb-10 mt-10 flex h-[400px] w-[100%] flex-row justify-center">
          <LineChart :chart-data="data" :options="options" class="flex h-full w-[50%]" ref="pageChart"></LineChart>

          <div class="flex flex-col justify-center p-20 align-middle text-white">
            <div class="mb-6 flex flex-row justify-center">
              <div class="mr-6 w-fit">
                <input @click="axis = 'x'" type="radio" id="x" name="axis" value="x" checked />
                <label for="x">Eixo X</label>
              </div>

              <div class="w-fit">
                <input @click="axis = 'y'" type="radio" id="y" name="axis" value="y" />
                <label for="y">Eixo Y</label>
              </div>
            </div>

            <div v-if="axis == 'x'">
              <div class="text-black">
                <div class="mb-4 flex flex-row justify-center">
                  <div class="mr-4 flex w-20 items-center text-white">Mínimo:</div>
                  <input class="input w-30 flex rounded-md border-2 border-black p-1" id="graph_min" type="number" />
                </div>

                <div class="mb-4 flex flex-row justify-center">
                  <div class="mr-4 flex w-20 items-center text-white">Máximo:</div>
                  <input class="input w-30 flex rounded-md border-2 border-black p-1" id="graph_max" type="number" />
                </div>

                <div class="mb-4 flex flex-row justify-center">
                  <div class="mr-4 flex w-20 items-center text-white">Step:</div>
                  <input
                    class="input w-30 flex rounded-md border-2 border-black p-1"
                    id="graph_stepsize"
                    type="number" />
                </div>

                <div class="mb-4 flex flex-row justify-center">
                  <button
                    @click="graphRangeX"
                    class="mb-6 mt-4 h-fit w-60 rounded-lg border-2 border-white p-1 font-bold text-white">
                    Modificar
                  </button>
                </div>
              </div>
            </div>

            <div v-if="axis == 'y'">
              <div class="flex-col text-black">
                <div class="mb-4 flex flex-row justify-center">
                  <div class="mr-4 flex w-20 items-center text-white">Mínimo:</div>
                  <input class="input w-30 flex rounded-md border-2 border-black p-1" id="graph_min_y" type="text" />
                </div>

                <div class="mb-4 flex flex-row justify-center">
                  <div class="mr-4 flex w-20 items-center text-white">Máximo:</div>
                  <input class="input w-30 flex rounded-md border-2 border-black p-1" id="graph_max_y" type="text" />
                </div>

                <div class="mb-4 flex flex-row justify-center">
                  <div class="mr-4 flex w-20 items-center text-white">Step:</div>
                  <input
                    class="input w-30 flex rounded-md border-2 border-black p-1"
                    id="graph_stepsize_y"
                    type="text" />
                </div>

                <div class="mb-4 flex flex-row justify-center">
                  <button
                    @click="graphRangeY"
                    class="mb-6 mt-4 h-fit w-60 rounded-lg border-2 border-white p-1 font-bold text-white">
                    Modificar
                  </button>
                </div>
              </div>
            </div>

            <div class="flex w-full justify-center">
              <button
                @click="resetGraph"
                class="mb-6 mt-4 h-fit w-40 rounded-lg border-2 border-white p-1 font-bold text-white">
                Apagar curvas
              </button>
            </div>
          </div>
        </div>

        <div class="ml-10 mr-10 flex w-full flex-row">
          <div class="cpouso-content flex w-[50%] flex-col items-center justify-center">
            <span class="mb-10 text-xl font-semibold text-white">Criar curvas de pouso suave</span>
            <div class="flex flex-col items-center text-black">
              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Curva:</div>
                <input class="input mr-4 rounded-md p-1" id="ps_curva_cor" type="color" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Label:</div>
                <input class="input rounded-md border-2 border-black p-1" id="ps_label" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Massa:</div>
                <input class="input rounded-md border-2 border-black p-1" id="ps_massa" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Gravidade:</div>
                <input class="input rounded-md border-2 border-black p-1" id="ps_gravidade" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Intensidade:</div>
                <input class="input rounded-md border-2 border-black p-1" id="ps_intensidade" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Ângulo:</div>
                <input class="input rounded-md border-2 border-black p-1" id="ps_angulo" type="text" />
              </div>
            </div>
            <button
              @click="curvaPousoSuave"
              class="mb-6 mt-4 h-fit w-60 rounded-lg border-2 border-white p-1 font-bold text-white">
              Calcular
            </button>
          </div>

          <div class="cvel-content flex w-[50%] flex-col items-center">
            <span class="mb-10 text-xl font-semibold text-white">Criar curvas de velocidade</span>
            <div class="flex flex-row items-center text-black">
              <div class="mb-4 flex flex-row md:mr-4 xl:mr-4">
                <div class="mr-4 items-center text-white first-line:flex">Curva:</div>
                <input class="input mr-4 rounded-md p-1" id="cv_curva_cor" type="color" />
              </div>

              <div class="mb-4 flex flex-row md:mr-4 xl:mr-4">
                <div class="mr-4 items-center text-white first-line:flex">Ponto:</div>
                <input class="input rounded-md p-1" id="cv_point_cor" type="color" />
              </div>
            </div>
            <div class="mr-28 flex flex-col items-end">
              <div class="mb-4 flex flex-row">
                <div class="mr-4 items-center text-white first-line:flex">Label:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_label" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 items-center text-white first-line:flex">Altura inicial:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_altura_inicial" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 items-center text-white first-line:flex">Velocidade inicial:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_velocidade_inicial" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 items-center text-white first-line:flex">Massa:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_massa" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 items-center text-white first-line:flex">Gravidade:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_gravidade" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 w-20 items-center text-white first-line:flex">Intensidade:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_intensidade" type="text" />
              </div>

              <div class="mb-4 flex flex-row">
                <div class="mr-4 items-center text-white first-line:flex">Ângulo:</div>
                <input class="input rounded-md border-2 border-black p-1" id="cv_angulo" type="text" />
              </div>
            </div>
            <button
              @click="curvaVelocidade"
              class="mb-6 mt-4 h-fit w-60 rounded-lg border-2 border-white p-1 font-bold text-white">
              Calcular
            </button>
          </div>
        </div>

        <div class="h-28"></div>
      </div>

      <div v-show="twolines">
        <div class="mb-10 ml-6 mt-10 flex flex-row">
          <div class="ml-6 mr-6 cursor-pointer content-center">
            <svg
              @click="(twolines = false), (explore = true)"
              class="h-6 w-6 scale-125 text-gray-800 dark:text-white"
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
                d="m15 19-7-7 7-7" />
            </svg>
          </div>
          <div class="w-fit content-center text-3xl font-bold text-white">Two Lines (Powered by Celestrak)</div>
        </div>

        <div class="flex flex-col items-center">
          <a class="mb-6"><img src="https://i.imgur.com/0p4MmcU.png" title="tle" /></a>
        </div>

        <div class="cont-search-content ml-10 mr-10 mt-4 flex-col">
          <select
            @input="selectGroupCelestrak($event.target.value)"
            class="mb-8 w-full rounded-md p-3"
            name="celestrak-group">
            <option selected disabled hidden>Selecione um grupo</option>
            <option v-for="item in celestrakGroups" :value="item.code">{{ item.name }}</option>
          </select>

          <div v-if="selectedGroup != null">
            <select
              @input="selectObjectCelestrak($event.target.value)"
              class="w-full rounded-md p-3"
              name="celestrak-object">
              <option selected disabled hidden>Selecione um veículo espacial</option>
              <option v-for="item in celestrakObjects" :value="item.OBJECT_NAME">{{ item.OBJECT_NAME }}</option>
            </select>
          </div>
          <div v-else>
            <select class="w-full rounded-md p-3" disabled>
              <option selected disabled hidden>Selecione um veiculo espacial</option>
            </select>
          </div>

          <div v-if="selectedObject != null">
            <div class="bgblack mt-6 rounded-md p-4">
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Argumento do Perigeu:</div>
                <input
                  :value="selectedObject.ARG_OF_PERICENTER"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">BStar:</div>
                <input :value="selectedObject.BSTAR" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Classificação:</div>
                <input
                  :value="selectedObject.CLASSIFICATION_TYPE"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Excentricidade:</div>
                <input :value="selectedObject.ECCENTRICITY" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Element Set No:</div>
                <input
                  :value="selectedObject.ELEMENT_SET_NO"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Tipo de ephemeris:</div>
                <input
                  :value="selectedObject.EPHEMERIS_TYPE"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Epoch:</div>
                <input :value="selectedObject.EPOCH" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Inclinação:</div>
                <input :value="selectedObject.INCLINATION" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Anomalia Média:</div>
                <input :value="selectedObject.MEAN_ANOMALY" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Movimento Médio:</div>
                <input :value="selectedObject.MEAN_MOTION" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Movimento Médio DDot:</div>
                <input
                  :value="selectedObject.MEAN_MOTION_DDOT"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Movimento Médio Dot:</div>
                <input
                  :value="selectedObject.MEAN_MOTION_DOT"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">NORAD CAT ID:</div>
                <input :value="selectedObject.NORAD_CAT_ID" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Object ID:</div>
                <input :value="selectedObject.OBJECT_ID" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Object Name:</div>
                <input :value="selectedObject.OBJECT_NAME" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">RA do Nodo ascendente:</div>
                <input
                  :value="selectedObject.RA_OF_ASC_NODE"
                  class="bgblue flex-1 rounded-md p-2"
                  type="text"
                  disabled />
              </div>
              <div class="mb-4 flex flex-col text-gray-300 md:flex-row xl:flex-row">
                <div class="mr-4 w-full">Rev at Epoch:</div>
                <input :value="selectedObject.REV_AT_EPOCH" class="bgblue flex-1 rounded-md p-2" type="text" disabled />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Modal from '@/components/Modal'
import UserModal from '@/components/UserModal'
import LineChart from './LineChart.vue'
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
      axis: 'x',
      userModal: false,
      modalSolarSystema: false,
      modalPosicionamento: false,
      modalManobras: false,
      modalLagrange: false,
      modalPousoLunar: false,
      modalCelestrak: false,
      prefix: {
        home: 'selected',
        explore: ''
      },
      celestrakGroups: [
        { code: 'last-30-days', name: 'Last 30 days' },
        { code: 'stations', name: 'Space Stations' },
        { code: 'visual', name: '100 (or so) Brightest' },
        { code: 'iridium-33-debris', name: 'Iridium 33 Debris' },
        { code: 'weather', name: 'Weather Satellites' },
        { code: 'starlink', name: 'Starlink Satellites' },
        { code: 'intelsat', name: 'Intelsat Satellites' },
        { code: 'iridium', name: 'Iridium Satellites' },
        { code: 'orbcomm', name: 'Orbcomm Satellites' },
        { code: 'cubesat', name: 'Cubesats' },
        { code: 'radar', name: 'Radar Calibration' },
        { code: 'planet', name: 'Planet Labs' }
      ],
      celestrakObjects: [],
      selectedGroup: null,
      selectedObject: null,
      home: true,
      pousoLunar: false,
      twolines: false,
      explore: false,
      signin: true,
      register: false,
      loggedin: false,
      data: {
        datasets: []
      },
      options: {
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
            min: -20,
            max: 10, // Define o range do eixo x
            ticks: {
              stepSize: 2, // Define o intervalo entre os ticks
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
            min: -20,
            max: 10, // Define o range do eixo x
            ticks: {
              stepSize: 2, // Define o intervalo entre os ticks
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
  created() {
    // window.location.hash = 'home'
    // window.addEventListener('popstate', () => {
    //     const hash = window.location.hash.substring(1)
    //     const menu = ['home', 'explore']
    //     menu.forEach((item) => {
    //         this.prefix[item] = ''
    //         this[item] = false
    //     })
    //     this[hash] = true
    //     this.prefix[hash] = 'selected'
    // })
  },
  methods: {
    async selectGroupCelestrak(code) {
      this.selectedGroup = code
      this.celestrakObjects = null
      console.log(code)

      const rawResponse = await fetch(
        `https://celestrak.org/NORAD/elements/gp.php?GROUP=${code}&FORMAT=json-pretty`,
        {}
      )

      const content = await rawResponse.json()
      this.celestrakObjects = content
    },
    selectObjectCelestrak(code) {
      this.selectedObject = _.find(this.celestrakObjects, { OBJECT_NAME: code })
    },
    // menu(ref){
    //     this.userModal = false
    //     this.pousoLunar = false
    //     this.twolines = false

    //     const menu = ['home', 'explore']

    //     menu.forEach((item) => {
    //         this.prefix[item] = ''
    //         this[item] = false
    //     })

    //     this.prefix[ref] = 'selected'
    //     this[ref] = true
    // },
    contentHS(baseClass) {
      let className = document.getElementsByClassName(baseClass)[0].className
      let classContent = document.getElementsByClassName(baseClass + '-content')[0].className

      if (className.includes('180')) {
        className = className.replace('rotate-180', 'rotate-0')
        document.getElementsByClassName(baseClass)[0].className = className
        classContent = classContent.replace('hidden', 'flex flex-col')
        document.getElementsByClassName(baseClass + '-content')[0].className = classContent
      } else {
        className = className.replace('rotate-0', 'rotate-180')
        document.getElementsByClassName(baseClass)[0].className = className
        classContent = classContent.replace('flex flex-col', 'hidden')
        document.getElementsByClassName(baseClass + '-content')[0].className = classContent
      }
    },
    graphRangeX() {
      const min = parseFloat(document.getElementById('graph_min').value)
      const max = parseFloat(document.getElementById('graph_max').value)
      const stepsize = parseFloat(document.getElementById('graph_stepsize').value)

      this.options.scales.x.min = min
      this.options.scales.x.max = max
      this.options.scales.x.ticks.stepSize = stepsize
      this.options.scales.x.type = 'linear'

      const pageChart = this.$refs.pageChart
      pageChart.update()
    },
    graphRangeY() {
      const min = parseFloat(document.getElementById('graph_min_y').value)
      const max = parseFloat(document.getElementById('graph_max_y').value)
      const stepsize = parseFloat(document.getElementById('graph_stepsize_y').value)

      this.options.scales.y.min = min
      this.options.scales.y.max = max
      this.options.scales.y.ticks.stepSize = stepsize
      this.options.scales.y.type = 'linear'

      const pageChart = this.$refs.pageChart
      pageChart.update()
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
    resetGraph() {
      this.data.datasets = []
      const pageChart = this.$refs.pageChart
      pageChart.update()
    },
    async curvaPousoSuave() {
      const corCurva = document.getElementById('ps_curva_cor').value
      const nome = document.getElementById('ps_label').value
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
          angulacao: angulacao
        })
      })

      const content = await rawResponse.json()
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

      this.data.datasets.push(newDataset)

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

        this.data.datasets.push(newPoint)
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
      const index = this.data.labels.reduce((prevIndex, label, i) => {
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
      this.data.datasets.push(newDataset)
      // Atualizar o gráfico
      const pageChart = this.$refs.pageChart
      pageChart.update()
    },
    async curvasPousoSuave() {
      const rawResponse = await fetch('/pouso/lunar/suave', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
        },
        body: JSON.stringify({
          massa: 1.1,
          gravidade: 1.8,
          intensidade: 3.6,
          angulacao: 0,
          altura: 18,
          velocidade_inicial: -7
        })
      })

      const content = await rawResponse.json()
      return content

      // {
      //             label: ,
      //             data: [65, 59, 80, 81, 56, 55, 100],
      //             fill: false,
      //             borderColor: 'rgb(75, 192, 192)',
      //             tension: 0.4,
      //         },
    },
    linspace(start, end, n) {
      const step = (end - start) / (n - 1)
      const result = []
      for (let i = 0; i < n; i++) {
        result.push((start + i * step).toFixed(1))
      }
      return result
    }
  }
}
</script>
