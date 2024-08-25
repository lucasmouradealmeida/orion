from flask import Blueprint

from server.core.context import Context
from server.decorators import with_context
from server.resources.app_resource import AppConfig

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"], endpoint="home")
@with_context(template="./home.html")
def home_controller(ctx: Context):
    from server.services.admin_service import article_service

    artigos = article_service.all_articles(ctx)
    config = {
        "core": "home",
        "module": "home",
        "layout": "template_home",
        "context": {
            "artigos": artigos,
        },
    }
    return {"titulo": "Home", "app": AppConfig(**config).to_dict()}
