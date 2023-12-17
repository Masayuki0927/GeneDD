from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def hello():
    html = render_template('index.html', aa = 'masayuki')
    return html

@app.route("/calc", methods=["post"])
def calc():
    # 受け取った値を掛け算する
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a * b
    return render_template('output.html', answer = r)

if __name__ == '__main__':
    app.run(debug=True)
