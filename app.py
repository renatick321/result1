from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def label():
    return "<strong>Миссия Колонизация планет</strong>"

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def promotion_image(nickname, level, rating):
    return render_template("index.html", level=level, rating=rating, nickname=nickname)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')