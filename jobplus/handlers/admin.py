from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix='/admin')


@admin.route("/")
def index():
    return "管理后台"
