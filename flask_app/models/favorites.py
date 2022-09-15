from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Favorite:
    def __init__(self, data):
        self.user_favorite = data['user_favorite_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']


        #LEFT JOIN
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.kind_of_user = data['kind_of_user']
        self.content = data['content']


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO favarites(user_favorite_id, post_id) VALUES (%(user_favorite_id)s, %(post_id)s)"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result


    @classmethod
    def get_users_favorite(cls, formulario):
        query = "SELECT posts.content,posts.created_at, posts.id, favarites.*, users.first_name, users.last_name, users.kind_of_user, users.id as user_id FROM posts JOIN favarites ON favarites.post_id = posts.id JOIN users ON users.id = posts.user_id WHERE user_favorite_id = %(id)s ORDER BY favarites.created_at desc"
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        favorite = []
        for i in results:
            favorite.append(cls(i))
        return favorite

    @classmethod
    def eliminar_favoritos(cls, formulario):
        query = "DELETE favarites FROM favarites WHERE user_favorite_id = %(user_favorite_id)s AND post_id = %(post_id)s; "
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        return results

