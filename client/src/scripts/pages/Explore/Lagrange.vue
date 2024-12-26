<template>
  <div class="mb-10 px-6">
    <div class="text-white">
      <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Pontos de Lagrange</div>
    </div>

    <!-- Detalhes -->
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
              <p class="mb-4 text-lg text-gray-700">
                Os
                <strong class="font-bold text-gray-900">pontos de equilíbrio de Lagrange</strong>
                são pontos específicos no espaço onde a força gravitacional de dois corpos principais se equilibra com a
                força centrífuga experimentada por um objeto que se move com eles. Esses pontos são importantes em
                mecânica celeste e astrodinâmica e são usados para posicionar satélites e sondas espaciais.
              </p>

              <h2 class="mb-4 mt-6 text-2xl font-semibold text-gray-800">Características dos Pontos Lagrangeanos</h2>
              <p class="mb-4 text-lg text-gray-700">
                Existem cinco pontos de Lagrange, numerados de
                <strong class="font-bold text-gray-900">L1 a L5</strong>
                , e eles têm diferentes características de estabilidade e de velocidade:
              </p>

              <div class="space-y-6">
                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L1 - Ponto de Equilíbrio Instável</h3>
                  <p class="text-lg text-gray-700">
                    Localizado entre os dois corpos (como a Terra e o Sol), o ponto L1 é o mais utilizado para missões
                    espaciais. Um objeto neste ponto tem a velocidade orbital igual à dos corpos principais e permanece
                    "parado" em relação ao sistema de referência. No entanto, o ponto L1 é instável, ou seja, pequenas
                    perturbações podem fazer com que o objeto se desvie. A curva de velocidade zero neste ponto define a
                    linha de equilíbrio de velocidade.
                  </p>
                </div>

                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L2 - Ponto de Equilíbrio Instável</h3>
                  <p class="text-lg text-gray-700">
                    Localizado do lado oposto ao L1, fora da órbita dos corpos principais. Embora o objeto também tenha
                    velocidade zero neste ponto, o L2 é instável e, assim como o L1, pequenas alterações podem desviar o
                    objeto.
                  </p>
                </div>

                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L3 - Ponto de Equilíbrio Instável</h3>
                  <p class="text-lg text-gray-700">
                    Fica do lado oposto ao ponto L1, na direção da órbita dos corpos principais. Este ponto é instável e
                    não seria utilizado para posicionamento de objetos de forma estável.
                  </p>
                </div>

                <div>
                  <h3 class="text-xl font-semibold text-gray-800">L4 e L5 - Pontos de Equilíbrio Estáveis</h3>
                  <p class="text-lg text-gray-700">
                    Estes pontos estão localizados ao longo da órbita dos corpos principais, formando um triângulo
                    equilátero com os corpos. Objetos nestes pontos podem ter uma velocidade zero em relação ao sistema
                    de referência e, devido à sua estabilidade, não precisam de ajustes contínuos para permanecer no
                    ponto.
                  </p>
                </div>
              </div>

              <h2 class="mb-4 mt-6 text-2xl font-semibold text-gray-800">Curvas de Velocidade Zero</h2>
              <p class="mb-4 text-lg text-gray-700">
                A curva de velocidade zero descreve as regiões onde a velocidade do objeto é zero no referencial
                rotativo dos dois corpos. Em outras palavras, é a condição em que o objeto pode ficar parado em relação
                ao sistema de referência sem precisar de velocidade adicional para se manter ali.
              </p>

              <div class="mt-6">
                <h3 class="mb-2 text-xl font-semibold text-gray-800">Resumo das Curvas de Velocidade Zero</h3>
                <ul class="list-disc space-y-2 pl-5 text-lg text-gray-700">
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
  </div>
</template>

<script>
export default {
  name: 'PontosLagrange',
  components: {},
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen
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
