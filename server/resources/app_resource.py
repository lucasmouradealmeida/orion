from server.core.base_model import BaseModel


class AppConfig(BaseModel):
    core: str | None = None
    module:  str | None = None
    layout: str | None = "template_undefined"
    context: dict | None = None