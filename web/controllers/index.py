# _*_ coding:utf-8 _*_

from flask import Blueprint,render_template

route_index = Blueprint('index', __name__)

@route_index.route("/")
def index():
    return render_template("index/index.html")
