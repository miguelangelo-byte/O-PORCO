from flask import Flask as flk
from flask import render_template, request
import mysql.connector as sql
from SQLcodes import *
import random
import os
senhas=os.getenv("DB_PASSWORD", "")

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

@app.route("/home")
def principal():
    return render_template("Home.html")

@app.route("/sobre")
def sobre():
    return "teste"

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
    return render_template("logteste.html", texto=bananildo)

@app.route("/verificarteste", methods=["GET", "POST"])
def adm():
    if request.method == "POST":
        db.execute("truncate table Usuario")
    db.execute(ver_adm)
    xadm = db.fetchall()
    return render_template("DBTeste.html", usuarios=xadm)

#just a joke with my friends, pls ignore commit 5 and later don't have this :P
@app.route("/homeMALIGNA", methods=["GET", "POST"])
def principalMALIGNO():
    teste = "teste"
    if request.method == "POST":
        x = random.randint(1, 100)
        if x < 3:
            teste = "sim"
        else:
            teste = "não"
    return render_template("HomeM.html", teste=teste)

if __name__ == "__main__":
    app.run(debug=True, port=5001)