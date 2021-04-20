# description: views
# date: 2021/2/4 12:31 下午
# author: objcat
# version: 1.0

from flask import Blueprint

normal = Blueprint(__name__, __name__)

@normal.route("/hello")
def hello():
    return {"name": "张三"}