from flask import Flask, jsonify, request
from .router.index import app as index
from .router.about import app as about

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# 当前项目文件夹
app.config["ROOT_DIR"] = "api"

app.register_blueprint(index, url_prefix="/api")
app.register_blueprint(about, url_prefix="/api")


@app.errorhandler(404)
def page_not_found(error):
    return jsonify(code=404, data=None, err=str(error))
