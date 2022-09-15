from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #LEFT JOIN
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.kind_of_user = data['kind_of_user']


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO posts(content, user_id) VALUES (%(content)s, %(user_id)s)"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result
    

    @classmethod
    def get_users_post(cls, formulario):
        query = "SELECT  users.first_name, users.last_name, users.kind_of_user, posts.* FROM posts LEFT JOIN users ON users.id = posts.user_id WHERE users.id = %(id)s ORDER BY posts.created_at desc"
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        post = []
        for i in results:
            post.append(cls(i))
        return post

    @classmethod
    def eliminar_post(cls, formulario):
        query = "DELETE FROM posts WHERE id = %(id)s" 
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result

    @classmethod
    def get_all_post(cls):
        query = "SELECT users.id as usersid, users.first_name, users.last_name, users.kind_of_user, posts.* FROM posts LEFT JOIN users ON users.id = posts.user_id ORDER BY posts.created_at desc"
        result = connectToMySQL('spaceweb').query_db(query)
        posts = []
        for post in result:
            posts.append(cls(post))
        return posts

    @classmethod
    def updated_post(cls, formulario):
        query = "SELECT  users.first_name, users.last_name, users.kind_of_user, posts.* FROM posts LEFT JOIN users ON users.id = posts.user_id WHERE posts.id = %(post_id)s ORDER BY posts.created_at desc"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        post = cls(result[0])
        return post

    @classmethod
    def actualizar(cls,formulario):
        query = "UPDATE posts SET content = %(content)s  WHERE id = %(id)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result