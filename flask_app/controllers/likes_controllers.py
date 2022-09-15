from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify, Response
from flask_app.models.users import User
from flask_app.models.posts import Post
from flask_app.models.likes import Like
from flask_app.models.unions import Union

@app.route("/likes", methods=['POST'])
def likes():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    
    formulario = {
        "liker_id": session['user_id'],
        "post_id": request.form["post_id"]
    }
    Like.save(formulario)
    numero = Like.updated_likes(formulario)
    return redirect('/wall')

@app.route("/delete/like/<int:id>")
def elimnar_likes(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario =  {
        "user_favorite_id":session['user_id'],
        "post_id": id
    }
    Like.eliminar_likes(formulario)
    return redirect('/likes/')

@app.route("/likes/people/<int:id>")
def likes_all_post(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "post_id": id,
        "id": session['user_id']
    }
    id = session['user_id']
    user = User.get_by_id(formulario)
    likes = Union.likes_people(formulario)
    return render_template("people_likes.html", likes = likes, user = user)