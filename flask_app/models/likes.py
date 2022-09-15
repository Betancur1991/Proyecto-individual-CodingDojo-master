from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Like:
    def __init__(self, data):
        self.liker_id = data['liker_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']
        self.likes = data['likes'] 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO likes(liker_id, post_id) VALUES (%(liker_id)s, %(post_id)s)"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result

    @classmethod
    def get_users_likes(cls):
        query = "SELECT COUNT(id) as likes, post_id, liker_id, likes.created_at FROM posts LEFT JOIN likes ON posts.id = likes.post_id group by post_id "
        results = connectToMySQL('spaceweb').query_db(query)
        like = []
        for likes in results:
            like.append(cls(likes))
        return like

    @classmethod
    def likes_post(cls,formulario):
        query = "SELECT *, likes.post_id as likes FROM likes WHERE post_id = %(post_id)s "
        results = connectToMySQL('spaceweb').query_db(query,formulario)
        like = []
        for likes in results:
            like.append(cls(likes))
        return like

    @classmethod
    def updated_likes(cls, formulario):
        query = "SELECT COUNT(post_id) as count_like FROM likes WHERE post_id = %(post_id)s "
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        print(results)
        return results[0]['count_like']

    @classmethod
    def get_user_like(cls, formulario):
        query = "SELECT *, likes.post_id as likes FROM likes WHERE liker_id = %(id)s "
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        favorite = []
        for i in results:
            favorite.append(cls(i))
        return favorite


    @classmethod
    def eliminar_likes(cls, formulario):
        query = "DELETE likes FROM likes WHERE liker_id = %(user_favorite_id)s AND post_id = %(post_id)s "
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        return results




