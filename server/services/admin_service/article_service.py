import pydash as py_

from server.core.context import Context


def all_articles(ctx: Context) -> list:
    """Artigos do site

    Args:
        ctx (Context): Contexto da requisição

    Returns:
        list: Lista de artigos
    """
    return [
    {
        "id": "1",
        "page": "home",
        "titulo": "Sobre",
        "conteudo": {
            "introducao_1": {
                "descricao": "Este projeto tem como intuito passar alguns dos conhecimentos aprendidos ao longo da graduação em Engenharia Aeroespacial. Campo que incorpora o estado da arte da engenharia aplicada ao projeto, análise, construção e testes de sistemas associados com o Setor Aeroespacial, envolvendo aeronaves, foguetes e satélites artificiais. Seus conhecimentos incluem sistemas de propulsão, comunicação, controle de aeronaves, navegação e interação homem-máquina. As tecnologias que este profissional utilizará são complementadas com noções de sensores e instrumentação de bordo, de materiais especiais, de aerodinâmica e de controle de temperatura. A formação na UFABC possibilita amplos conhecimentos de física, química, matemática, computação e noções fundamentais de engenharia."
            }
        }
    },
    {
        "id": "2",
        "page": "home",
        "titulo": "Perfil do profissional",
        "conteudo": {
            "introducao_1": {
                "descricao": "É o engenheiro apto a atuar em modelagem, controle, projeto, análise, construção e testes de sistemas no setor aeroespacial. Atuação: Pesquisa científica nas várias entidades que estudam aeronaves e veículos espaciais no Brasil (UFABC, INPE, CTA, AEB,...) Indústria: qualquer empresa que presta serviço ao setor aeroespacial (EMBRAER, AVIBRAS, Helibrás, etc). Empresário autônomo como fabricante/fornecedor de peças, componentes, serviços e soluções para o mercado aeroespacial brasileiro."
            }
        }
    },
    {
        "id": "3",
        "page": "home",
        "titulo": "Atuação profissional",
        "conteudo": {
            "introducao_1": {
                "descricao": "Desenvolvimento e a avaliação de sistemas diversos (computação, eletrônicos, mecânicos, hidráulicos) associados a aeronaves, foguetes e sondas espaciais. Desenvolvimento de satélites artificiais (modelagem, controle,...) para diversas finalidades (satélites meteorológicos, de comunicação, observacionais). Sistemas de propulsão, comunicação, controle de atitude, navegação, interação homem-máquina,... Sensores e instrumentação de bordo, materiais especiais, aerodinâmica, controle de temperatura, controle de vibração, em sistemas diversos associados a aeronaves, foguetes,..."
            }
        }
    },
    {
        "id": "4",
        "page": "home",
        "titulo": "Formação na UFABC",
        "conteudo": {
            "introducao_1": {
                "descricao": "Para a sua formação como Engenheiro Espacial, nosso curso oferece as seguintes disciplinas: Aerodinâmica, Aeroelasticidade, Astrodinâmica, Aviônica, Ciência dos Materiais, Controle de aeronaves, Desempenho, Ensaios em vôo, Estabilidade de vôo, Helicópteros, Instrumentação e sistemas, Propulsão, Sistemas de radar. Ao longo do curso, também serão estudados: Circuitos elétricos, Estruturas, Gestão, Matemática, Mecânica clássica, Mecânica dos Ruídos, Mecânica dos sólidos, Probabilidades e Estatística, Telecomunicações, Termodinâmica e Vibrações e ruído."
            }
        }
    },
    {
        "id": "5",
        "page": "twolines",
        "titulo": "Two-Line Element Set",
        "conteudo": {
            "introducao_1": {
                "descricao": "O formato de dados Two-Line Element Set (TLE) é um padrão amplamente utilizado para representar a órbita de objetos em torno da Terra, como satélites artificiais e detritos espaciais. Ele é disponibilizado por várias fontes, sendo o CelesTrak uma das mais conhecidas. Cada TLE contém dois conjuntos de linhas que fornecem informações detalhadas sobre a órbita do objeto, incluindo sua inclinação, excentricidade, argumento do perigeu, e outros parâmetros essenciais.",
                "image": "https://i.imgur.com/0p4MmcU.png",
            },
            "estrutura_2": {
                "descricao": "O TLE é composto por três linhas: 1. Linha 0 (Opcional): Nome do objeto. 2. Linha 1: Informações gerais, como número do satélite, época da órbita (data e tempo), e parâmetros que indicam a taxa de decaimento orbital. 3. Linha 2: Parâmetros orbitais, como inclinação, excentricidade, longitude do nodo ascendente, argumento do perigeu, anomalia média e o período orbital.",
            },
            "relevancia_3": {
                "descricao": "Os dados contidos no TLE são fundamentais para a dinâmica e controle de veículos espaciais, por várias razões: 1. Previsão de Órbita: Os TLEs permitem prever a posição de um satélite em sua órbita em um dado instante. Isso é crucial para a programação de manobras orbitais, como correções de órbita e ajustes de altitude, garantindo que o satélite permaneça na posição desejada para cumprir sua missão. 2. Planejamento de Missões: Para missões que envolvem interações com outros satélites, como aproximação, acoplamento ou desvio de colisão, o TLE fornece as informações necessárias para calcular os momentos e posições exatas dos objetos. Isso permite planejar manobras de maneira eficiente e segura.",
            },
            "evitacao_colisoes_4": {
                "descricao": "Em um ambiente espacial cada vez mais congestionado, com milhares de satélites e detritos em órbita, o TLE é essencial para evitar colisões. Sistemas de rastreamento de satélites e análise de tráfego espacial utilizam TLEs para identificar possíveis conflitos e coordenar manobras evasivas.",
            },
            "simulacoes_modelagem_5": {
                "descricao": "No desenvolvimento e teste de algoritmos de controle para veículos espaciais, os TLEs são usados em simulações para modelar o ambiente orbital e prever o comportamento do veículo em resposta a diferentes comandos de controle. Isso é essencial para validar a robustez dos sistemas de controle antes do lançamento.",
            },
            "atualizacoes_regulares_6": {
                "descricao": "O CelesTrak e outras fontes fornecem atualizações frequentes dos TLEs, refletindo mudanças nas órbitas devido a perturbações, como arrasto atmosférico e efeitos gravitacionais de outros corpos celestes. Isso permite que os operadores de satélites ajustem suas previsões e controlem seus veículos de maneira precisa e atualizada.",
            },
            "limitacoes_desafios_7": {
                "descricao": "Apesar de sua utilidade, o TLE tem limitações. A precisão dos dados diminui com o tempo desde a última atualização, o que significa que, para previsões a longo prazo, pode ser necessário usar modelos mais complexos de propagação orbital. Além disso, o TLE é baseado em um modelo simplificado da órbita terrestre (SGP4), que não leva em conta perturbações mais sutis, como pressão de radiação solar em certos cenários.",
            },
            "conclusao_8": {
                "descricao": "O TLE é uma ferramenta fundamental na área de dinâmica e controle de veículos espaciais, fornecendo dados críticos para a previsão de órbitas, planejamento de missões e evitação de colisões. Embora tenha suas limitações, sua simplicidade e acessibilidade o tornam uma peça-chave na operação de satélites e na gestão de tráfego espacial. A integração dos TLEs em sistemas de controle e simulação continua a ser um aspecto vital para o sucesso das missões espaciais."
            }
        }
    }


    ]

def articles_by_id(ctx: Context, id: int) -> list | None:
    """Artigos do site

    Args:
        ctx (Context): Contexto da requisição

    Returns:
        list | None: Lista de artigos
    """

    artigos = all_articles(ctx)

    return py_.filter_(artigos, lambda x: x["id"] == str(id))