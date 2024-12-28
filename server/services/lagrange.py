import astropy.units as u
import numpy as np
from astropy.coordinates import get_body
from astropy.time import Time
from matplotlib import pyplot as plt

from server.resources.lagrange_resource import LagrangePointsResource, LagrangePointsResult


def points_lagrange(data: LagrangePointsResource) -> LagrangePointsResult:
    """Calcula os pontos de Lagrange.

    Args:
        data (LagrangePointsResource): Dados de entrada.

    Returns:
        dict: Dados de retorno.
    """
    # Corpo celeste 1
    corpo1 = data.corpo1

    # Corpo celeste 2
    corpo2 = data.corpo2

    # Distancia entre os corpos celestes
    time = Time.now()

    # Obter as coordenadas dos corpos celestes
    body1 = get_body(corpo1, time)
    body2 = get_body(corpo2, time)

    distance = body1.separation_3d(body2)
    distancia_km = distance.to(u.km).max().value

    # Massa do corpo 1
    m1 = max(data.massa1, data.massa2)
    # Corpo celeste de maior massa
    corpo_maior = data.corpo1 if data.massa1 > data.massa2 else data.corpo2

    # Massa do corpo 2
    m2 = min(data.massa1, data.massa2)
    # Corpo celeste de menor massa
    corpo_menor = data.corpo1 if data.massa1 < data.massa2 else data.corpo2

    # Distância entre os corpos celestes
    r12 = distancia_km

    # Massa reduzida
    mi = m2 / (m1 + m2)

    # Localização dos Pontos Lagrangianos
    # Pontos L4 e L5
    L4 = [-mi + 0.5, np.sqrt(3) / 2]
    L5 = [L4[0], -L4[1]]

    # Pontos L1, L2 & L3
    rt = np.zeros((5, 1))
    x = -100
    k = 0
    c = 5

    # Teorema de Bolzano
    while k < c:
        f0 = x - (((1 - mi) / (abs(x + mi) ** 3)) * (x + mi)) - ((mi / (abs(x - 1 + mi) ** 3)) * (x - 1 + mi))
        x += 0.005
        f1 = x - (((1 - mi) / (abs(x + mi) ** 3)) * (x + mi)) - ((mi / (abs(x - 1 + mi) ** 3)) * (x - 1 + mi))

        if f0 > 0 and f1 < 0:
            rt[k, 0] = x - 0.005
            k += 1
        elif f1 > 0 and f0 < 0:
            rt[k, 0] = x - 0.005
            k += 1

    Er = 10**-8
    z = 0
    Lx = np.ones((3, 1))

    # Método de Newton-Raphson
    for i in range(0, 5, 2):
        x0 = rt[i, 0]
        Erx = 1

        while Erx > Er:
            fx = x0 - (((1 - mi) / (abs(x0 + mi) ** 3)) * (x0 + mi)) - ((mi / (abs(x0 - 1 + mi) ** 3)) * (x0 - 1 + mi))

            fx_d = (
                ((3 * mi * ((mi + x0 - 1) ** 2)) / (abs(mi + x0 - 1) ** 5))
                - ((mi) / (abs(mi + x0 - 1) ** 3))
                - ((1 - mi) / (abs(mi + x0) ** 3))
                + ((3 * (1 - mi) * ((mi + x0) ** 2)) / (abs(mi + x0) ** 5))
                + (1)
            )

            x = x0 - (fx / fx_d)
            Erx = abs(x0 - x) / abs(x)
            x0 = x

        Lx[z, 0] = x
        z += 1

    # Curvas de Velocidade Zero

    # Constante Gravitacional
    G = 1
    # Sol
    G * (1 - mi)
    # Júpiter
    mi2 = G * mi

    CL1 = 3 + (3 ** (3 / 4)) * (mi2 ** (2 / 3)) - ((10 * mi2) / 3)
    CL2 = 3 + (3 ** (3 / 4)) * (mi2 ** (2 / 3)) - ((14 * mi2) / 3)
    CL3 = 3 + mi2
    CL4 = 3 - mi2
    CL5 = CL4

    # Cj - Valores Corrigidos para o sistema em análise
    CLj = [CL1, CL2, CL3, CL4, CL5]

    # Plot dos gráficos
    j = 0.01
    k = 2

    x_range = np.arange(-k, k + j, j)
    y_range = np.arange(-k, k + j, j)
    X, Y = np.meshgrid(x_range, y_range)

    # Calcular Z uma vez fora do loop
    Z_base = X**2 + Y**2 + 2 * (((1 - mi) / np.sqrt((X + mi) ** 2 + Y**2)) + (mi / np.sqrt((X - 1 + mi) ** 2 + Y**2)))

    # Gerar múltiplos valores de Cj interpolados
    min_Cj = min(CLj) - 0.1  # Menor valor com margem
    max_Cj = max(CLj) + 0.1  # Maior valor com margem
    CJ_values = np.linspace(min_Cj, max_Cj, 15)  # valores de Cj para contorno

    par_ordenado = []

    for Cj in CJ_values:
        Z = Z_base - Cj

        # Plotando e extraindo os contornos
        CS = plt.contour(X * r12, Y * r12, Z * r12, levels=[0])  # Apenas o contorno onde Z = 0

        # Extraindo os pontos do contorno
        for collection in CS.collections:
            for path in collection.get_paths():
                v = path.vertices  # Pontos do contorno
                x_points = v[:, 0]
                y_points = v[:, 1]

                # Adicionando os pares ordenados com o valor de Cj
                pares = [[x, y] for x, y in zip(x_points, y_points)]
                par_ordenado.append({"Cj": Cj, "pontos": pares})

    # Multiplicar as posições dos Pontos Lagrangianos por r12
    L4_scaled = [coord * r12 for coord in L4]
    L5_scaled = [coord * r12 for coord in L5]
    L1_scaled = [Lx[1, 0] * r12, 0]
    L2_scaled = [Lx[2, 0] * r12, 0]
    L3_scaled = [Lx[0, 0] * r12, 0]
    L_scaled = [L1_scaled, L2_scaled, L3_scaled, L4_scaled, L5_scaled]

    return LagrangePointsResult(
        L_scaled=L_scaled,
        par_ordenado=par_ordenado,
        distancia=r12,
        corpo_maior=corpo_maior,
        corpo_menor=corpo_menor,
    )
