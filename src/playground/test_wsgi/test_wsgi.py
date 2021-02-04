# description: test_wsgi
# date: 2021/2/4 23:06
# author: objcat
# version: 1.0

from wsgiref.simple_server import make_server


def hello(env, res):
    res("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('hello world wsgi', encoding="utf-8")]


s = make_server('localhost', 8000, hello)
s.serve_forever()
