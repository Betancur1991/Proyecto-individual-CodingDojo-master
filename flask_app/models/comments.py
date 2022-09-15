from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Comment:
    def __init__(self, data):
        self.user_id_comment = data['user_id_comment']
        self.post_id_comment = data['post_id_comment']
        self.content = data['content']
        self.ceated_at = data['ceated_at']


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO comments(user_id_comment, post_id_comment, content) VALUES (%(user_id_comment)s, %(post_id_comment)s, %(content)s)"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result

    @classmethod
    def seleccionar_commen(cls, formulario):
        query = "SELECT  * FROM comments WHERE user_id_comment = %(user_id_comment)s AND post_id_comment = %(post_id_comment)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        post = cls(result[0])
        return post

    @classmethod
    def actualizar_comment(cls,formulario):
        query = "UPDATE comments SET content = %(content)s  WHERE user_id_comment = %(user_id_comment)s AND post_id_comment = %(post_id_comment)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result