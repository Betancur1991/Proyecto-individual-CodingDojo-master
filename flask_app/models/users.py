from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from random import randrange

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.kind_of_user = data['kind_of_user']
        self.email = data['email']
        self.password = data['password']
        self.life = data['life']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, kind_of_user, email, password, life) VALUES (%(first_name)s, %(last_name)s, %(kind_of_user)s, %(email)s, %(password)s, %(life)s)"
        result = connectToMySQL('spaceweb').query_db(query, formulario) #regresa el nuevo id de la persona registrada 
        return result

    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        error=[]
        #Validar que el nombre tenga al menos 3 caracteres
        if len(formulario['first_name']) < 2:
            #flash('You must enter the name', 'registro')
            es_valido = False
            error.append('You must enter the name')
        
        if len(formulario['last_name']) < 2 :
            #flash('You must enter the last name', 'registro')
            es_valido = False
            error.append('You must enter the last name')


        #verificar que el email tenga formato correcto EXPRESIONES REGULARES
        if not EMAIL_REGEX.match(formulario['email']):
            #flash("invalid email", 'registro')
            es_valido = False
            error.append('invalid email')

        #Password con al menos 3 caracteres
        if len(formulario['password']) < 8 :
            #flash('The password must have at least 8 characters', 'registro')
            es_valido = False
            error.append('The password must have at least 8 characters')

        #Verificar que las contraseñas coincidan
        if formulario['password'] != formulario['confirma_password']:
            #flash('Passwords do not match','registro')
            error.append('Passwords do not match')

        #Consultar si ya existe ese correo electronico
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('spaceweb').query_db(query, formulario)
        if len(results) >= 1:
            #flash('Previously registered email', 'registro')
            es_valido = False
            error.append('Previously registered email')
        
        if formulario["kind_of_user"] == "Choose an option":
            flash('you must choose between the options', 'registro')
            es_valido = False
            error.append('you must choose between the options')
        return es_valido,error

    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario) #Regresa una lista 
        if len(result) < 1: #se pregunta por el tamaño del diccionario que el query regresa, si es menor a 1 es porque no contiene datospor lo que el email no ha sido registrado previamente
            return False
        else:
            user = cls(result[0])
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        user = cls(result[0])
        return user


    @classmethod
    def actualizar_profile(cls,formulario):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, kind_of_user = %(kind_of_user)s, life = %(life)s  WHERE id = %(id)s"
        result = connectToMySQL('spaceweb').query_db(query, formulario)
        return result
