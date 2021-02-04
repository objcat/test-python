# description: __init__.py
# date: 2021/2/4 12:26 下午
# author: objcat
# version: 1.0

from flask import Flask
from playground.test_flask.src.normal.views import normal
from playground.test_flask.src.admin.views import admin

app = Flask(__name__)

app.register_blueprint(normal, url_prefix="/api/v1")
app.register_blueprint(admin, url_prefix="/api/v1/admin")

