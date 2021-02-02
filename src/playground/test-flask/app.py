# description: app
# date: 2021/2/2 21:50
# author: objcat
# version: 1.0


from flask import Flask, render_template

# 创建flask
app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


# flask往页面上扔数据
@app.route("/hello")
def index2():
    s = "哈哈哈哈"
    return render_template("hello.html", s=s)


if __name__ == '__main__':
    app.run(debug=True)

# 模板
