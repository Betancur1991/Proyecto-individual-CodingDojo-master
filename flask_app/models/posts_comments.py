from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Postcomment:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.kind_of_user = data['kind_of_user']
        self.user_id_comment = data['user_id_comment']
        self.post_id_comment = data['post_id_comment']
        self.content = data['content']
        self.ceated_at = data['ceated_at']

    @classmethod
    def comments_people(cls):
        query = "SELECT  users.first_name, users.last_name, users.kind_of_user, comments.* FROM comments JOIN users ON users.id = comments.user_id_comment join posts on posts.id = post_id_comment"
        results = connectToMySQL('spaceweb').query_db(query)
        comments = []
        for comment in results:
            comments.append(cls(comment))
        return comments

    @classmethod
    def eliminar_comments(cls, formulario):
        query = "DELETE comments FROM comments WHERE user_id_comment = %(user_id_comment)s AND post_id_comment = %(post_id_comment)s "
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        return results
