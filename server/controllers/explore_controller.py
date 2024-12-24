from flask import Blueprint

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
