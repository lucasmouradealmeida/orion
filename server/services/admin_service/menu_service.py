from server.core.context import Context
from server.resources.admin_resources import Menu


def menu(ctx: Context) -> list[Menu] | None:
    """Opções de menu.

    Returns:
        list[Menu] | None: Lista de links das páginas do sistema.
    """
    return Menu.from_collection(
        [
            {"name": "Home", "icon": "Home", "url": "/"},
            {
                "name": "Explore",
                "icon": "Explore",
                "submenu": [
                    {"name": "Two Lines", "icon": "twolines", "url": "/twolines"},
                    {"name": "Pouso Lunar", "icon": "pousolunar", "url": "/pousolunar"},
                    {"name": "Transferência Orbital", "icon": "transforbital", "url": "/orbital"},
                    {"name": "Pontos de Lagrange", "icon": "pontoslagrange", "url": "/lagrange"},
                ],
            },
        ]
    )
