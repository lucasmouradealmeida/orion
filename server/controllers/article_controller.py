import pydash as py_
from flask import Blueprint

from server.core.context import Context
from server.decorators import with_context
from server.resources.app_resource import AppConfig

bp = Blueprint("article", __name__)


@bp.route("/article/<int:id>", methods=["GET"], endpoint="article")
@with_context(template="./article.html")
def article_controller(ctx: Context, id: int):
    from server.services.admin_service import article_service

    artigo = article_service.articles_by_id(ctx, id)

    config = {
        "core": "article",
        "module": "article",
        "layout": "template_article",
        "context": py_.get(artigo, "[0]", {}),
    }
    return {"titulo": "Article", "app": AppConfig(**config).to_dict()}
