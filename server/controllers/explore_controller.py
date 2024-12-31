from flask import Blueprint, jsonify

from server.core.context import Context
from server.decorators import with_context
from server.resources.app_resource import AppConfig

bp = Blueprint("explore", __name__)


@bp.route("/pousolunar", methods=["GET"], endpoint="pousolunar")
@with_context(template="./pousolunar.html")
def pousolunar_controller(ctx: Context):
    return {"titulo": "Pouso Lunar"}


@bp.route("/lagrange", methods=["GET"], endpoint="pontos-lagrange")
@with_context(template="./pontos-lagrange.html")
def pontos_lagrange_controller(ctx: Context):
    return {"titulo": "Pontos de Lagrange"}


@bp.route("/lagrange/points", methods=["POST"], endpoint="calcular-pontos-lagrange")
@with_context()
def calculate_lagrange_points_controller(ctx: Context):
    from server.resources.lagrange_resource import LagrangePointsResource
    from server.services.lagrange import points_lagrange

    kwargs = ctx.request.json
    data = LagrangePointsResource(**kwargs)
    result = points_lagrange(data)

    converted_L = [list(map(float, L)) for L in result.L_scaled]

    return jsonify(
        L=converted_L,
        par_ordenado=result.par_ordenado,
        corpo_maior=result.corpo_maior,
        corpo_menor=result.corpo_menor,
        distancia=result.distancia,
    )


@bp.route("/orbital", methods=["GET"], endpoint="transferencia-orbital")
@with_context(template="./transferencia-orbital.html")
def transferencia_orbital_controller(ctx: Context):
    return {"titulo": "Transferência Orbital"}


@bp.route("/twolines", methods=["GET"], endpoint="twolines")
@with_context(template="./twolines.html")
def twolines_controller(ctx: Context):
    from server.services.celestrak_service import celestrak_service

    all_groups = celestrak_service.get_groups(ctx)

    config = {
        "core": "article",
        "module": "article",
        "layout": "template_article",
        "context": {
            "groups": all_groups,
        },
    }
    return {"titulo": "Two Lines", "app": AppConfig(**config).to_dict()}


@bp.route("/groundtrack", methods=["GET"], endpoint="groundtrack")
@with_context(template="./ground-track.html")
def ground_track_controller(ctx: Context):
    return {"titulo": "Ground Track"}
