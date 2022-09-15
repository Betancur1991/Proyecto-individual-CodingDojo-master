from flask_app import app
from flask import render_template, redirect, request, session
#Importar bcrypt para codificar la contraseña


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/singup")
def signup():
    return render_template("singup.html")

@app.route("/wall")
def wall():
    return render_template("wall.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")