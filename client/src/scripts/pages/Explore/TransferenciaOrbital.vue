<template>
  <div class="px-6">
    <div class="text-white">
      <div class="mb-1 mt-6 pl-4 text-[22pt] font-bold text-white">Transferência Orbital</div>
    </div>

    <!-- Tabs -->
    <div class="mx-5 my-4 overflow-x-auto rounded-full bg-white p-1">
      <nav class="flex flex-nowrap gap-6" aria-label="Tabs">
        <a
          @click="
            (flagHohmann = true),
              (flagTriImpulsiva = false),
              (flagNaoCoplanar = false),
              (flagRendezvous = false),
              (flagPatchedConics = false),
              (isOpen = false)
          "
          :class="
            flagHohmann
              ? 'bg-[#324AB2] font-bold text-white'
              : 'font-medium text-black hover:font-bold hover:text-[#324AB2]'
          "
          class="shrink-0 cursor-pointer rounded-full p-2 text-sm">
          Hohmann
        </a>
        <a
          @click="
            (flagTriImpulsiva = true),
              (flagHohmann = false),
              (flagNaoCoplanar = false),
              (flagRendezvous = false),
              (flagPatchedConics = false),
              (isOpen = false)
          "
          :class="
            flagTriImpulsiva
              ? 'bg-[#324AB2] font-bold text-white'
              : 'font-medium text-black hover:font-bold hover:text-[#324AB2]'
          "
          class="shrink-0 cursor-pointer rounded-full p-2 text-sm">
          Tri Impulsiva
        </a>
        <a
          @click="
            (flagNaoCoplanar = true),
              (flagHohmann = false),
              (flagTriImpulsiva = false),
              (flagRendezvous = false),
              (flagPatchedConics = false),
              (isOpen = false)
          "
          :class="
            flagNaoCoplanar
              ? 'bg-[#324AB2] font-bold text-white'
              : 'font-medium text-black hover:font-bold hover:text-[#324AB2]'
          "
          class="shrink-0 cursor-pointer rounded-full p-2 text-sm">
          Não Coplanar
        </a>
        <a
          @click="
            (flagRendezvous = true),
              (flagHohmann = false),
              (flagTriImpulsiva = false),
              (flagNaoCoplanar = false),
              (flagPatchedConics = false),
              (isOpen = false)
          "
          :class="
            flagRendezvous
              ? 'bg-[#324AB2] font-bold text-white'
              : 'font-medium text-black hover:font-bold hover:text-[#324AB2]'
          "
          class="shrink-0 cursor-pointer rounded-full p-2 text-sm">
          Rendezvous
        </a>
        <a
          @click="
            (flagPatchedConics = true),
              (flagHohmann = false),
              (flagTriImpulsiva = false),
              (flagNaoCoplanar = false),
              (flagRendezvous = false),
              (isOpen = false)
          "
          :class="
            flagPatchedConics
              ? 'bg-[#324AB2] font-bold text-white'
              : 'font-medium text-black hover:font-bold hover:text-[#324AB2]'
          "
          class="shrink-0 cursor-pointer rounded-full p-2 text-sm">
          Patched Conics
        </a>
      </nav>
    </div>

    <!-- Hohmann -->
    <div class="mb-10 px-4" v-if="flagHohmann">
      <!-- Descrição do módulo -->
      <div class="group">
        <div class="flex cursor-pointer items-center justify-between space-x-2 rounded" @click="toggle">
          <h2 class="text-medium w-max font-semibold text-white">Descrição</h2>

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
            <p class="text-justify">
              A transferência de Hohmann é uma manobra orbital extremamente eficiente para economizar combustível, sendo
              ideal para transferências entre duas órbitas circulares, concêntricas e coplanares. Essa estratégia
              utiliza dois impulsos: o primeiro para inserir a espaçonave em uma órbita elíptica de transferência
              tangente às órbitas inicial e final, e o segundo para circularizar a trajetória na órbita final. No
              entanto, sua eficiência depende da razão entre o raio da órbita final e o raio da órbita inicial. Essa
              técnica é mais vantajosa quando essa razão é menor que 11,94, pois, para valores superiores, outras
              manobras, como transferências bi-elíptica tri-impulsiva, podem se tornar mais econômicas em termos de Δv
              (variação de velocidade). Assim, a transferência de Hohmann é amplamente utilizada em situações onde as
              órbitas envolvidas estão relativamente próximas, sendo uma solução simples e eficiente.
            </p>
          </div>
        </transition>
      </div>

      <!-- Conteúdo da seção -->
      <div class="flex flex-row">
        <div class="mt-10 flex flex-col gap-4 px-6">
          <div class="select-planets">
            <label for="planet-select" class="mr-4 text-white">Selecione um corpo celeste:</label>

            <select id="planet-select" class="rounded-lg p-2" v-model="selectedPlanet">
              <option v-for="planet in planets" :key="planet.name" :value="planet">
                {{ planet.name }}
              </option>
            </select>

            <div v-if="selectedPlanet" class="mt-2 text-white">
              <p>
                <strong>Planeta Selecionado:</strong>
                {{ selectedPlanet.name }}
              </p>
              <p>
                <strong>µ (G x M):</strong>
                {{ selectedPlanet.mu.toExponential(2) }} m³/s²
              </p>
            </div>
          </div>

          <!-- Raio 1 -->
          <div class="mt-4 space-x-3">
            <label for="raio1" class="text-white">Raio 1 (km):</label>
            <input id="raio1" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Raio 2 -->
          <div class="mt-4 space-x-3">
            <label for="raio2" class="text-white">Raio 2 (km):</label>
            <input id="raio2" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Calcular -->
          <div class="mt-4">
            <button @click="calcularHohmann" class="rounded-lg bg-[#324AB2] p-2 text-white">Calcular</button>
          </div>
        </div>

        <!-- Resultados -->
        <div v-if="flagResultadoHohmann" class="mt-10 flex flex-col gap-4 px-6 text-white">
          <div>
            <strong>Variação de Velocidade 1 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade 2 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade Total (km/s):</strong>
            {{ velocidadeTotal }}
          </div>

          <div>
            <strong>Tempo de Transferência:</strong>
            {{ tempoTransferencia }}
          </div>
        </div>
      </div>
    </div>

    <!-- Tri Impulsiva -->
    <div class="mb-10 px-4" v-if="flagTriImpulsiva">
      <!-- Descrição do módulo -->
      <div class="group">
        <div class="flex cursor-pointer items-center justify-between space-x-2 rounded" @click="toggle">
          <h2 class="text-medium w-max font-semibold text-white">Descrição</h2>

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
            <p class="text-justify">
              A manobra tri-impulsiva, ou transferência bi-elíptica, é uma alternativa à transferência de Hohmann para
              trajetórias orbitais envolvendo duas órbitas circulares e coplanares. Conforme demonstrado por Hoelker e
              Silber, essa manobra torna-se mais eficiente em termos de Δv (variação de velocidade) quando a razão entre
              o raio final e o raio inicial da órbita é maior que 11,94. Nesses casos, a transferência tri-impulsiva
              pode economizar combustível em comparação com a transferência de Hohmann, apesar de ser mais complexa e
              exigir três impulsos: dois para inserir e ajustar a órbita intermediária elíptica e um terceiro para
              circularizar a órbita final. Essa abordagem é especialmente vantajosa em missões onde a diferença entre as
              órbitas é significativamente grande, destacando-se por sua eficiência em trajetórias de longa distância.
            </p>
          </div>
        </transition>
      </div>

      <!-- Conteúdo da seção -->
      <div class="flex flex-row">
        <div class="mt-10 flex flex-col gap-4 px-6">
          <div class="select-planets">
            <label for="planet-select" class="mr-4 text-white">Selecione um corpo celeste:</label>

            <select id="planet-select" class="rounded-lg p-2" v-model="selectedPlanet">
              <option v-for="planet in planets" :key="planet.name" :value="planet">
                {{ planet.name }}
              </option>
            </select>

            <div v-if="selectedPlanet" class="mt-2 text-white">
              <p>
                <strong>Planeta Selecionado:</strong>
                {{ selectedPlanet.name }}
              </p>
              <p>
                <strong>µ (G x M):</strong>
                {{ selectedPlanet.mu.toExponential(2) }} m³/s²
              </p>
            </div>
          </div>

          <!-- Raio 1 -->
          <div class="mt-4 space-x-3">
            <label for="raio1" class="text-white">Raio 1 (km):</label>
            <input id="raio1" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Raio 2 -->
          <div class="mt-4 space-x-3">
            <label for="raio2" class="text-white">Raio 2 (km):</label>
            <input id="raio2" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Apogeu -->
          <div class="mt-4 space-x-3">
            <label for="apogeu" class="text-white">Apogeu (km):</label>
            <input id="apogeu" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Calcular -->
          <div class="mt-4">
            <button @click="calcularTriImpulsiva" class="rounded-lg bg-[#324AB2] p-2 text-white">Calcular</button>
          </div>
        </div>

        <!-- Resultados -->
        <div v-if="flagResultadoTriImpulsiva" class="mt-10 flex flex-col gap-4 px-6 text-white">
          <div>
            <strong>Variação de Velocidade 1 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade 2 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade Total (km/s):</strong>
            {{ velocidadeTotal }}
          </div>

          <div>
            <strong>Tempo de Transferência:</strong>
            {{ tempoTransferencia }}
          </div>
        </div>
      </div>
    </div>

    <!-- Não coplanar -->
    <div class="mb-10 px-4" v-if="flagNaoCoplanar">
      <!-- Descrição do módulo -->
      <div class="group">
        <div class="flex cursor-pointer items-center justify-between space-x-2 rounded" @click="toggle">
          <h2 class="text-medium w-max font-semibold text-white">Descrição</h2>

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
            <p class="text-justify">
              A mudança de plano combinada é uma técnica utilizada para transferências orbitais entre órbitas circulares
              não coplanares, especialmente quando há diferença significativa entre os raios das órbitas. Essa abordagem
              pode ser realizada de duas maneiras: primeiro executando uma transferência de Hohmann seguida por uma
              mudança simples de plano orbital, ou começando com uma mudança de plano orbital seguida de uma
              transferência de Hohmann. Em ambas as estratégias, a manobra convencional requer três impulsos separados,
              resultando em maior consumo de Δv. Contudo, é possível otimizar a trajetória ao realizar a transferência
              com apenas duas queimas de motor, reduzindo o consumo de combustível e aumentando a eficiência da operação
              orbital.
            </p>
          </div>
        </transition>
      </div>

      <!-- Conteúdo da seção -->
      <div class="flex flex-row">
        <div class="mt-10 flex flex-col gap-4 px-6">
          <div class="select-planets">
            <label for="planet-select" class="mr-4 text-white">Selecione um corpo celeste:</label>

            <select id="planet-select" class="rounded-lg p-2" v-model="selectedPlanet">
              <option v-for="planet in planets" :key="planet.name" :value="planet">
                {{ planet.name }}
              </option>
            </select>

            <div v-if="selectedPlanet" class="mt-2 text-white">
              <p>
                <strong>Planeta Selecionado:</strong>
                {{ selectedPlanet.name }}
              </p>
              <p>
                <strong>µ (G x M):</strong>
                {{ selectedPlanet.mu.toExponential(2) }} m³/s²
              </p>
            </div>
          </div>

          <!-- Raio 1 -->
          <div class="mt-4 space-x-3">
            <label for="raio1" class="text-white">Raio 1 (km):</label>
            <input id="raio1" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Raio 2 -->
          <div class="mt-4 space-x-3">
            <label for="raio2" class="text-white">Raio 2 (km):</label>
            <input id="raio2" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Ângulo 1 -->
          <div class="mt-4 space-x-3">
            <label for="graus1" class="text-white">Ângulo 1 (graus):</label>
            <input id="graus1" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Ângulo 2 -->
          <div class="mt-4 space-x-3">
            <label for="graus2" class="text-white">Ângulo 2 (graus):</label>
            <input id="graus2" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Calcular -->
          <div class="mt-4">
            <button @click="calcularNaoCoplanar" class="rounded-lg bg-[#324AB2] p-2 text-white">Calcular</button>
          </div>
        </div>

        <!-- Resultados -->
        <div v-if="flagResultadoNaoCoplanar" class="mt-10 flex flex-col gap-4 px-6 text-white">
          <div>
            <strong>Variação de Velocidade 1 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade 2 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade Total (km/s):</strong>
            {{ velocidadeTotal }}
          </div>

          <div>
            <strong>Tempo de Transferência:</strong>
            {{ tempoTransferencia }}
          </div>
        </div>
      </div>
    </div>

    <!-- Rendezvous -->
    <div class="mb-10 px-4" v-if="flagRendezvous">
      <!-- Descrição do módulo -->
      <div class="group">
        <div class="flex cursor-pointer items-center justify-between space-x-2 rounded" @click="toggle">
          <h2 class="text-medium w-max font-semibold text-white">Descrição</h2>

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
            <p class="text-justify">
              A manobra de fase, também conhecida como *Rendezvous* Co-orbital, é uma técnica utilizada para sincronizar
              dois objetos em órbitas próximas, de modo que possam se encontrar no mesmo ponto da trajetória orbital.
              Essa manobra é baseada na transferência de Hohmann, consistindo em dois impulsos: o primeiro para alterar
              a órbita do objeto que realizará a aproximação e o segundo para ajustá-lo à órbita do alvo no momento do
              encontro. O diferencial dessa manobra é que ela é planejada para que o objeto que realiza o ajuste orbital
              retorne ao mesmo ponto inicial, garantindo uma convergência precisa com o alvo.
            </p>
          </div>
        </transition>
      </div>

      <!-- Conteúdo da seção -->
      <div class="flex flex-row">
        <div class="mt-10 flex flex-col gap-4 px-6">
          <div class="select-planets">
            <label for="planet-select" class="mr-4 text-white">Selecione um corpo celeste:</label>

            <select id="planet-select" class="rounded-lg p-2" v-model="selectedPlanet">
              <option v-for="planet in planets" :key="planet.name" :value="planet">
                {{ planet.name }}
              </option>
            </select>

            <div v-if="selectedPlanet" class="mt-2 text-white">
              <p>
                <strong>Planeta Selecionado:</strong>
                {{ selectedPlanet.name }}
              </p>
              <p>
                <strong>µ (G x M):</strong>
                {{ selectedPlanet.mu.toExponential(2) }} m³/s²
              </p>
            </div>
          </div>

          <!-- Apoastro -->
          <div class="mt-4 space-x-3">
            <label for="apoastro" class="text-white">Apoastro (km):</label>
            <input id="apoastro" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Periastro -->
          <div class="mt-4 space-x-3">
            <label for="raio2" class="text-white">Periastro (km):</label>
            <input id="raio2" type="text" class="rounded-lg p-2" />
          </div>

          <!-- Calcular -->
          <div class="mt-4">
            <button @click="calcularRendezvous" class="rounded-lg bg-[#324AB2] p-2 text-white">Calcular</button>
          </div>
        </div>

        <!-- Resultados -->
        <div v-if="flagResultadoRendezvous" class="mt-10 flex flex-col gap-4 px-6 text-white">
          <div>
            <strong>Variação de Velocidade 1 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade 2 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade Total (km/s):</strong>
            {{ velocidadeTotal }}
          </div>

          <div>
            <strong>Tempo de Transferência:</strong>
            {{ tempoTransferencia }}
          </div>
        </div>
      </div>
    </div>

    <!-- Patched Conics -->
    <div class="mb-10 px-4" v-if="flagPatchedConics">
      <!-- Descrição do módulo -->
      <div class="group">
        <div class="flex cursor-pointer items-center justify-between space-x-2 rounded" @click="toggle">
          <h2 class="text-medium w-max font-semibold text-white">Descrição</h2>

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
            <p class="text-justify">
              A manobra Patched Conics é um método utilizado em mecânica orbital para simplificar a modelagem de
              trajetórias de naves espaciais ao considerar apenas dois corpos celestes em interação direta em cada etapa
              da viagem. Em vez de calcular a interação gravitacional entre todos os corpos presentes no sistema, a
              técnica divide a trajetória em "patches" ou segmentos, onde, em cada um, a nave é tratada como se
              estivesse sob a influência gravitacional de apenas um corpo (como a Terra, por exemplo, ou a Lua) enquanto
              se desloca. A manobra é útil especialmente em missões interplanetárias ou transferências orbitais, como as
              manobras de transferência de Hohmann, já que permite uma descrição precisa e prática da trajetória, sem a
              necessidade de resolver equações dinâmicas complexas para o sistema completo. O método facilita a análise
              de trajetórias em múltiplos corpos ao desconsiderar interações que acontecem em distâncias mais longas,
              concentrando-se nas interações que realmente afetam a nave em cada fase da viagem.
            </p>
          </div>
        </transition>
      </div>

      <!-- Conteúdo da seção -->
      <div class="flex flex-row">
        <div class="mt-10 flex flex-col gap-4 px-6">
          <div class="select-planets">
            <label for="select-1" class="mr-4 text-white">Primeiro corpo celeste:</label>
            <select id="select-1" class="rounded-lg p-2" v-model="selectedBody1" @change="checkForSun">
              <option value="" disabled selected>Selecione um corpo celeste</option>
              <option v-for="body in celestialBodies" :key="body" :value="body">{{ body }}</option>
            </select>
          </div>

          <div class="select-planets">
            <label for="select-2" class="mr-4 text-white">Segundo corpo celeste:</label>
            <select id="select-2" class="rounded-lg p-2" v-model="selectedBody2" @change="checkForSun">
              <option value="" disabled selected>Selecione um corpo celeste</option>
              <option v-for="body in celestialBodies" :key="body" :value="body">{{ body }}</option>
            </select>
          </div>

          <div v-if="considerSun" class="mt-2 text-white">
            <p>O Sol deve ser considerado na manobra de Patched Conics.</p>
          </div>

          <!-- Calcular -->
          <div class="mt-4">
            <button @click="calcularPatchedConics" class="rounded-lg bg-[#324AB2] p-2 text-white">Calcular</button>
          </div>
        </div>

        <!-- Resultados -->
        <div v-if="flagResultadoPatchedConics" class="mt-10 flex flex-col gap-4 px-6 text-white">
          <div>
            <strong>Variação de Velocidade 1 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade 2 (km/s):</strong>
            {{ velocidadeTransferencia }}
          </div>

          <div>
            <strong>Variação de Velocidade Total (km/s):</strong>
            {{ velocidadeTotal }}
          </div>

          <div>
            <strong>Tempo de Transferência:</strong>
            {{ tempoTransferencia }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TransferenciaOrbital',
  components: {},
  data() {
    const G = 6.6743e-11 // Constante gravitacional universal (m³/kg/s²)

    // Dados dos planetas: nome e massa em kg
    const planets = [
      { name: 'Mercúrio', mass: 3.3011e23 },
      { name: 'Vênus', mass: 4.8675e24 },
      { name: 'Terra', mass: 5.97237e24 },
      { name: 'Marte', mass: 6.4171e23 },
      { name: 'Júpiter', mass: 1.8982e27 },
      { name: 'Saturno', mass: 5.6834e26 },
      { name: 'Urano', mass: 8.681e25 },
      { name: 'Netuno', mass: 1.02413e26 }
    ]

    // Calcula µ para cada planeta
    planets.forEach((planet) => {
      planet.mu = G * planet.mass
    })

    return {
      isOpen: false,
      planets,
      selectedPlanet: null,
      flagHohmann: true,
      flagTriImpulsiva: false,
      flagNaoCoplanar: false,
      flagRendezvous: false,
      flagPatchedConics: false,
      flagResultadoHohmann: false,
      flagResultadoTriImpulsiva: false,
      flagResultadoNaoCoplanar: false,
      flagResultadoRendezvous: false,
      flagResultadoPatchedConics: false,
      selectedBody1: '',
      selectedBody2: '',
      considerSun: false,
      planetsAndMoons: {
        Mercúrio: ['Mercúrio'],
        Vênus: ['Vênus'],
        Terra: ['Terra', 'Lua'],
        Marte: ['Marte', 'Fobos', 'Deimos'],
        Júpiter: ['Júpiter', 'Ío', 'Europa', 'Ganimedes', 'Calisto'],
        Saturno: ['Saturno', 'Titã', 'Rea', 'Mimas'],
        Urano: ['Urano', 'Miranda', 'Ariel'],
        Netuno: ['Netuno', 'Tritão']
      },
      celestialBodies: [
        // Planetas e Luas no Sistema Solar
        'Mercúrio',
        'Vênus',
        'Terra',
        'Marte',
        'Júpiter',
        'Saturno',
        'Urano',
        'Netuno',
        'Lua',
        'Fobos',
        'Deimos',
        'Ío',
        'Europa',
        'Ganimedes',
        'Calisto',
        'Titã',
        'Rea',
        'Mimas',
        'Miranda',
        'Ariel',
        'Tritão'
      ]
    }
  },
  methods: {
    checkForSun() {
      // Verifica se a lua selecionada pertence ao planeta selecionado
      if (this.selectedBody1 && this.selectedBody2) {
        const planetSelected = this.selectedBody1
        const moonSelected = this.selectedBody2

        // Se a lua selecionada pertence ao planeta selecionado, o Sol NÃO deve ser considerado
        if (this.planetsAndMoons[planetSelected]?.includes(moonSelected)) {
          this.considerSun = false
        } else {
          // Caso contrário, o Sol DEVE ser considerado
          this.considerSun = true
        }
      }
    },
    toggle() {
      this.isOpen = !this.isOpen
    },
    calcularHohmann() {
      // Calculo de velocidades e tempo de transferência
      this.flagResultadoHohmann = true
    },
    calcularTriImpulsiva() {
      // Calculo de velocidades e tempo de transferência
      this.flagResultadoTriImpulsiva = true
    },
    calcularNaoCoplanar() {
      // Calculo de velocidades e tempo de transferência
      this.flagResultadoNaoCoplanar = true
    },
    calcularRendezvous() {
      // Calculo de velocidades e tempo de transferência
      this.flagResultadoRendezvous = true
    },
    calcularPatchedConics() {
      // Calculo de velocidades e tempo de transferência
      this.flagResultadoPatchedConics = true
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
