from app.config.mysqlconnection import connectToMySQL
import datetime
from flask import flash


db = "queenflossy"
class Like:

    def __init__(self, data):
        self.likes = data['likes']
        self.post_id = data['post_id']
        self.users_id = data['users_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO likes (posts_id, users_id) VALUES (%(posts_id)s, %(users_id)s)"
        return connectToMySQL(db).query_db(query, data)
    
    @staticmethod
    def count_likes(posts_id):
        query = "SELECT COUNT(*) as count FROM likes WHERE postts_id = %(posts_id)s;"
        data = { 'posts_id': posts_id }
        result = connectToMySQL(db).query_db(query, data)
        return result[0]['count']
    
    @staticmethod
    def has_liked(data):
        query = "SELECT COUNT(*) as count FROM posts_has_likes WHERE users_id = %(users_id)s AND posts_id = %(posts_id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result[0]['count'] >= 1

    @staticmethod
    def unlike(data):
        query = "DELETE FROM likes WHERE users_id = %(users_id)s AND posts_id = %(posts_id)s;"
        return connectToMySQL(db).query_db(query, data)