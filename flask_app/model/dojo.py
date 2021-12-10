from werkzeug.wrappers import request
from flask_app.config.mysqlconnection import connectToMySQL
DB='dojos_and_ninjas'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ______________

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)
        dojos = []
        for name in results:
            dojos.append( cls(name) )
        return dojos

# _______________

    @classmethod
    def get_both(cls, data):
        query = 'SELECT * FROM dojos JOIN ninjas ON dojos.id = dojos_id WHERE dojos_id = %(id)s;'
        results = connectToMySQL(DB).query_db(query, data)
        return results

# ______________

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])

# ______________
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL(DB).query_db( query, data )    

from flask_app.config.mysqlconnection import connectToMySQL