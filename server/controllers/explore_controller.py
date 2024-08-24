from flask import Blueprint

from server.core.context import Context
from server.decorators import with_context

bp = Blueprint("explore", __name__)


@bp.route("/explore", methods=["GET"], endpoint="explore")
@with_context(template="./explore.html")
def explore_controller(ctx: Context):
    return {"titulo": "Explore"}
