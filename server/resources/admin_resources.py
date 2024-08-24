from server.core.base_model import BaseModel


class Menu(BaseModel):
    name: str
    icon: str | None = None
    url: str | None = None
    submenu: list["Menu"] | None = None