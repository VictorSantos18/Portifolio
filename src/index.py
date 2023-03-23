from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/inicio.html")
def inicio():
    return render_template("inicio.html")

@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")

@app.route("/habilidades.html")
def habilidades():
    return render_template("habilidades.html")

@app.route("/contato.html")
def contato():
    return render_template("contato.html")

@app.route("/trabalhos.html")
def trabalhos():
    return render_template("trabalhos.html")

