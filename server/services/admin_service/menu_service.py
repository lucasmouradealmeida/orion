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
                    {"name": "Módulo 1", "icon": "mod1", "url": "/mod1"},
                    {"name": "Módulo 2", "icon": "mod2", "url": "/mod2"},
                ],
            }
        ]
    )