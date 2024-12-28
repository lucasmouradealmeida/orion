from server.core.base_model import BaseModel


class LagrangePointsResource(BaseModel):
    corpo1: str
    corpo2: str
    massa1: float
    massa2: float


class LagrangePointsResult(BaseModel):
    L_scaled: list
    par_ordenado: list
    distancia: float
    corpo_maior: str
    corpo_menor: str
