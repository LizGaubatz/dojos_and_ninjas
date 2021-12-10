from werkzeug.wrappers import request
from flask_app.config.mysqlconnection import connectToMySQL
DB='dojos_and_ninjas'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ______________

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DB).query_db(query)
        all_users = []
        for user in results:
            all_users.append( cls(user) )
        return all_users


# ______________

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])

# ______________
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age, dojos_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojos_id)s, NOW() , NOW());"
        return connectToMySQL(DB).query_db( query, data )    

from flask_app.config.mysqlconnection import connectToMySQL