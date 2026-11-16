from flask import Flask as flk
from flask import render_template, request, redirect, session
import mysql.connector as sql
from SQLcodes import *
try:
    from senha import *
except ImportError:
    pass

ODB = sql.connect(
    host="localhost",
    user="root",
    password=senhas
)
db = ODB.cursor()
db.execute("create database if not exists porcodb")
ODB = sql.connect(
    host="localhost",
    user="root",
    database="porcodb",
    password=senhas
)
db = ODB.cursor()
db.execute(tabelausu)

app = flk(__name__)
app.secret_key = secret

@app.route("/")
def direcionar():
    return redirect("/home")

@app.route("/home")
def principal():
    return render_template("Home.html")

@app.route("/sobre")
def sobre():
    return render_template("Sobre.html")

@app.route("/cardapio", methods=["GET", "POST"])
def cardapio():
    verificar = ""
    if "carrinho2" not in session:
        session["carrinho2"] = 0
    if request.method == "POST":
        if "butao1" in request.form:
            session["carrinho2"] += 1
        if "apagar" in request.form:
            session["carrinho2"] = 0
        if "butaoTST" in request.form:
            verificar = "verde"
    return render_template("Cardapio.html", verificar=verificar, carrinho2=session["carrinho2"])

#para verificações passadas, não usado mais
@app.route("/inicioteste", methods=["GET", "POST"])
def principio():
    bananildo = ""
    if request.method == "POST":
        login = request.form.get("UsuarioLogin")
        senha = request.form.get("UsuarioSenha")
        db.execute(verificar, (login,))
        bananoviski = db.fetchone()
        if bananoviski is not None:
            bananildo = "Login ja existente"
        else:
            db.execute(pegar, (login, senha))
            ODB.commit()
            db.execute(ver)
            x = db.fetchone()
            bananildo = f"Ola {x[0]} e {x[1]}"
    return render_template("logTeste.html", texto=bananildo)

@app.route("/verificarteste", methods=["GET", "POST"])
def adm():
    if request.method == "POST":
        db.execute("truncate table Usuario")
    db.execute(ver_adm)
    xadm = db.fetchall()
    return render_template("DBTeste.html", usuarios=xadm)

if __name__ == "__main__":
    app.run(debug=True, port=5001)