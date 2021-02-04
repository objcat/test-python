# description: views.py
# date: 2021/2/4 12:40 下午
# author: objcat
# version: 1.0

from flask import Blueprint

admin = Blueprint(__name__, __name__)

@admin.route("/hello")
def hello():
    return "i am admin"