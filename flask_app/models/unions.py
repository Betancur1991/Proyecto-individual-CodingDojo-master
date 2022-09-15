from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Union:
    def __init__(self, data):
        self.liker_id = data['liker_id']
        self.post_id = data['post_id']
        self.created_at = data['created_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.kind_of_user = data['kind_of_user']


    @classmethod
    def likes_people(cls,formulario):
        query = "SELECT  users.first_name, users.last_name, users.kind_of_user, likes.* FROM likes JOIN users ON users.id = likes.liker_id WHERE post_id = %(post_id)s "
        results = connectToMySQL('spaceweb').query_db(query,formulario)
        like = []
        for likes in results:
            like.append(cls(likes))
        return like
