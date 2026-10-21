from flask import Flask as flk
from flask import render_template, request
import mysql.connector as sql
from SQLcodes import *
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
    pass

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
    return render_template("slakk.html", texto=bananildo)

@app.route("/verificarteste", methods=["GET", "POST"])
def adm():
    if request.method == "POST":
        db.execute("truncate table Usuario")
    db.execute(ver_adm)
    xadm = db.fetchall()
    return render_template("adm.html", usuarios=xadm)

if __name__ == "__main__":
    app.run(debug=True, port=5001)