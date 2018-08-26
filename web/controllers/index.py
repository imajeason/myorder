# _*_ coding:utf-8 _*_

from flask import Blueprint

route_index = Blueprint('index', __name__)

@route_index.route("/")
def index():
    return "Hello world." 
