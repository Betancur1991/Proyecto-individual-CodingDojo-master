from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify, Response
from flask_app.models.users import User
from flask_app.models.posts import Post
from flask_app.models.likes import Like
from flask_app.models.favorites import Favorite

@app.route("/favorite", methods=['POST'])
def favorites():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    
    formulario = {
        "user_favorite_id": session['user_id'],
        "post_id": request.form["post_id"]
    }
    Favorite.save(formulario)
    return Response(status = 204)

@app.route("/delete/favorite/<int:id>")
def elimnar_favoritos(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario =  {
        "user_favorite_id":session['user_id'],
        "post_id": id
    }
    Favorite.eliminar_favoritos(formulario)
    return redirect('/favorite')