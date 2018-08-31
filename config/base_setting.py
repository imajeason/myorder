# _*_ coding:utf-8 _*_

DEBUG =  False 
SERVER_PORT = 8000
SQLALCHEMY_ECHO = False 
SQLALCHEMY_DATABASE_URI = 'mysql://myorder:123456@localhost/mysql'
SQLALCHEMY_TRACK_MODIFICATIONS  =  False
SQLALCHEMY_ENCODING = "UTF-8"

PAGE_SIZE = 20
PAGE_DISPLAY= 10

AUTH_COOKIE_NAME = 'my_order'

#过滤url
IGNORE_URLS = [
  "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
  "^/static",
  "^/favicon.ico"
]
