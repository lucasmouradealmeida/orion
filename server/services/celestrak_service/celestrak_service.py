
from server.core.context import Context


def get_groups(ctx: Context) -> list:
    """Obter grupos de satélites

    Args:
        ctx (Context): Contexto da aplicação

    Returns:
        list: Lista de grupos de satélites
    """
    celestrakGroups = [
        { "code": 'last-30-days', "name": 'Last 30 days' },
        { "code": 'stations', "name": 'Space Stations' },
        { "code": 'visual', "name": '100 (or so) Brightest' },
        { "code": 'iridium-33-debris', "name": 'Iridium 33 Debris' },
        { "code": 'weather', "name": 'Weather Satellites' },
        { "code": 'starlink', "name": 'Starlink Satellites' },
        { "code": 'intelsat', "name": 'Intelsat Satellites' },
        { "code": 'iridium', "name": 'Iridium Satellites' },
        { "code": 'orbcomm', "name": 'Orbcomm Satellites' },
        { "code": 'cubesat', "name": 'Cubesats' },
        { "code": 'radar', "name": 'Radar Calibration' },
        { "code": 'planet', "name": 'Planet Labs' }
      ],
    return celestrakGroups