from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify, Response
from flask_app.models.users import User
from flask_app.models.posts import Post
from flask_app.models.likes import Like
from flask_app.models.comments import Comment
from flask_app.models.posts_comments import Postcomment

@app.route("/comentar", methods=['POST'])
def comments():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    
    formulario = {
        "user_id_comment": request.form["user_id_comment"],
        "post_id_comment": request.form["post_id_comment"],
        "content": request.form['content']
        
    }
    Comment.save(formulario)
    return redirect("/wall")


@app.route("/delete/comment/<int:id>")
def elimnar_comments(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario =  {
        "user_id_comment":session['user_id'],
        "post_id_comment": id
    }
    Postcomment.eliminar_comments(formulario)
    return redirect('/wall')

@app.route('/edit/comments/<int:id>')
def edit_comments(id):
    formulario ={
        "user_id_comment": session['user_id'],
        "post_id_comment" : id
    }
    formulario_2 ={
        "post_id": id,
        "id": session['user_id']
    }
    id = id
    user = User.get_by_id(formulario_2)
    comment = Comment.seleccionar_commen(formulario)
    return render_template("editar_comment.html", comment = comment, user = user)


@app.route('/updated_comments', methods=['POST'])
def updated_comment():
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "post_id_comment": request.form["post_id_comment"],
        "user_id_comment": request.form["user_id_comment"],
        "content": request.form["content"]
    }
    comment = Comment.actualizar_comment(formulario)
    return redirect ("/wall")