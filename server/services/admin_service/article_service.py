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
        "titulo": "Sobre",
        "conteudo": "Este projeto tem como intuito passar alguns dos conhecimentos aprendidos ao longo da graduação em Engenharia Aeroespacial. Campo que incorpora o estado da arte da engenharia aplicada ao projeto, análise, construção e testes de sistemas associados com o Setor Aeroespacial, envolvendo aeronaves, foguetes e satélites artificiais. Seus conhecimentos incluem sistemas de propulsão, comunicação, controle de aeronaves, navegação e interação homem-máquina. As tecnologias que este profissional utilizará são complementadas com noções de sensores e instrumentação de bordo, de materiais especiais, de aerodinâmica e de controle de temperatura. A formação na UFABC possibilita amplos conhecimentos de física, química, matemática, computação e noções fundamentais de engenharia."
    },
    {
        "id": "2",
        "titulo": "Perfil do profissional",
        "conteudo": "É o engenheiro apto a atuar em modelagem, controle, projeto, análise, construção e testes de sistemas no setor aeroespacial Atuação: Pesquisa científica nas várias entidades que estudam aeronaves e veículos espaciais no Brasil (UFABC, INPE, CTA, AEB,...) Indústria: qualquer empresa que presta serviço ao setor aeroespacial (EMBRAER, AVIBRAS, Helibrás, etc). Empresário autônomo como fabricante/fornecedor de peças, componentes, serviços e soluções para o mercado aeroespacial brasileiro."
    },
    {
        "id": "3",
        "titulo": "Atuação profissional",
        "conteudo": "Desenvolvimento e a avaliação de sistemas diversos (computação, eletrônicos, mecânicos, hidráulicos) associados a aeronaves, foguetes e sondas espaciais. Desenvolvimento de satélites artificiais (modelagem, controle,...) para diversas finalidades (satélites meteorológicos, de comunicação, observacionais) Sistemas de propulsão, comunicação, controle de atitude, navegação, interação homem-máquina,... Sensores e instrumentação de bordo, materiais especiais, aerodinâmica, controle de temperatura, controle de vibração, em sistemas diversos associados a aeronaves, foguetes,..."
    },
    {
        "id": "4",
        "titulo": "Formação na UFABC",
        "conteudo": "Para a sua formação como Engenheiro Espacial, nosso curso oferece as seguintes disciplinas: Aerodinâmica, Aeroelasticidade, Astrodinâmica, Aviônica, Ciência dos Materiais, Controle de aeronaves, Desempenho, Ensaios em vôo, Estabilidade de vôo, Helicópteros, Instrumentação e sistemas, Propulsão, Sistemas de radar. Ao longo do curso, também serão estudados: Circuitos elétricos, Estruturas, Gestão, Matemática, Mecânica clássica, Mecânica dos Ruídos, Mecânica dos sólidos, Probabilidades e Estatística, Telecomunicações, Termodinâmica e Vibrações e ruído."
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