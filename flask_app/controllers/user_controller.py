from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.users import User
from flask_app.models.posts import Post
from flask_app.models.likes import Like
from flask_app.models.favorites import Favorite
from flask_app.models.posts_comments import Postcomment


#Importar bcrypt para codificar la contraseña
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) # se crea una instancia de bcrypt

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/findout')
def findout():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    id = session['user_id']
    formulario = {
        "id":id
    }
    user = User.get_by_id(formulario)
    
    return render_template("findout.html", user = user)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/singup")
def signup():
    return render_template("singup.html")

@app.route("/signin", methods=['POST'])
def registrate():
    valida=User.valida_usuario(request.form)
    if not valida[0]:
        return jsonify(message=valida[1][0])
    else:
        pwd = bcrypt.generate_password_hash(request.form['password'])

        formulario = {  # se crea un nuevo formulario para poder agregar la nueva contraseña encriptada 
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "kind_of_user":request.form['kind_of_user'],
            "email":request.form['email'],
            "password":pwd,
            "life":request.form['life']
        }
        id = User.save(formulario) #recibo el id del nuevo usuario, a traves del query INSERT que nos arroja el id del nuevo usuario
        session['user_id'] = id # se guarda ese id nuevo en session
        
        return jsonify(message="correcto")

@app.route('/wall')
def wall():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": session['user_id']
    }
    id = session['user_id']
    user = User.get_by_id(formulario) #se crea una instancia por medio de la función get_by_id para tener todos los datos del nuevo usuario
    poster = Post.get_all_post()
    likes = Like.get_users_likes()
    comments = Postcomment.comments_people()
    return render_template("wall.html", user = user, poster = poster, id = id, likes = likes, comments = comments)


@app.route('/login-2', methods = ['POST'])
def inicio_sesion():
    #Verificar que el usuario exista, que el email exista
    user = User.get_by_email(request.form) #Estamos recibiendo una instancia de usuario o False
    if not user: # si se recibe False, se muestra el mensaje y se redirecciona a la pagina principal 
        return jsonify(message = "Wrong email")

    if not bcrypt.check_password_hash(user.password, request.form['password']): #para comparar una contraseña encriptada con otra que no lo esta 
        return jsonify(message = "Incorrect password")

    session['user_id'] = user.id # se crea una session al terminar el registro si toda sale bien 
    return jsonify(message="correcto") # se redirige al appointments


@app.route('/logout')
def cerrar_sesion():
    session.clear() #se eliminan todas las sessiones que se hallan guardado
    return redirect('/')


@app.route('/publicar', methods=['POST'])
def publicar():
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "user_id": session['user_id'],
        "content": request.form["content"]
    }
    post = Post.save(formulario)
    return redirect ("/profile")


@app.route('/profile')
def profile():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": session['user_id']
    }
    likes = Like.get_users_likes()
    user = User.get_by_id(formulario)
    post = Post.get_users_post(formulario)
    id_user = session['user_id']
    user2 = User.get_by_id(formulario)
    comments = Postcomment.comments_people()
    return render_template("profile.html", user = user, post = post, id_user = id_user, user2 = user2, likes = likes, comments = comments)


@app.route("/delete/<int:id>")
def eliminar(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario =  {
        "id": id
    }
    Post.eliminar_post(formulario)
    return redirect('/profile')

@app.route("/profile/<int:id>")
def profile_2(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": id
    }

    id_user = session['user_id']
    formulario_2 ={
        "id": id_user
    }
    likes = Like.get_users_likes()
    user = User.get_by_id(formulario)
    post = Post.get_users_post(formulario)
    user2 = User.get_by_id(formulario_2)
    return render_template("profile.html", user = user, post = post, id_user = id_user, user2 = user2, likes = likes)


@app.route('/favorite/')
def favorite():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": session['user_id']
    }
    id = session['user_id']
    user = User.get_by_id(formulario) #se crea una instancia por medio de la función get_by_id para tener todos los datos del nuevo usuario
    poster = Post.get_all_post()
    likes = Like.get_users_likes()
    favorite = Favorite.get_users_favorite(formulario)
    return render_template("favorite.html", user = user, poster = poster, id = id, likes = likes, favorite = favorite)

@app.route('/likes/')
def likes_all():
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": session['user_id']
    }
    id = session['user_id']
    user = User.get_by_id(formulario) #se crea una instancia por medio de la función get_by_id para tener todos los datos del nuevo usuario
    poster = Post.get_all_post()
    likes = Like.get_user_like(formulario)
    return render_template("likes.html", user = user, poster = poster, id = id, likes = likes)

@app.route("/edit/<int:id>")
def editar(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "post_id": id,
        "id": session['user_id']
    }
    id = id
    user = User.get_by_id(formulario)
    updated = Post.updated_post(formulario)
    return render_template("editar.html", updated = updated, user = user, id = id)

@app.route('/updated', methods=['POST'])
def updated():
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": request.form["id"],
        "content": request.form["content"]
    }
    post = Post.actualizar(formulario)
    return redirect ("/profile")


@app.route("/edit/profile/<int:id>")
def editar_profile(id):
    if 'user_id' not in session: #pregunta si user_id esta guardado en la session 
        return redirect('/')
    formulario = { # se crea un nuevo formulario para guardar el id del usuario 
        "id": id,
    }
    id = id
    user = User.get_by_id(formulario)
    return render_template("editar_template.html", user = user, )


@app.route('/updated_profile', methods=['POST'])
def updated_profile():
    User.actualizar_profile(request.form)
    return redirect ("/profile/"+ str(request.form['id']))