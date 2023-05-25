import datetime
from flask import flash
from app.config.mysqlconnection import connectToMySQL
from app.models import user


class Post:
    db = "queenflossy"

    def __init__(self, db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.posting = db_data['posting']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users on posts.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []
        for row in results:
            this_post = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": "",
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            this_post.creator = user.User(user_data)
            posts.append(this_post)
        return posts

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM posts JOIN users on posts.user_id = users.id WHERE posts.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(id)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (title, posting, user_id, created_at, updated_at) VALUES (%(title)s, %(posting)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, form_data):
        query = "UPDATE posts SET title=%(title)s, posting=%(posting)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, form_data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM posts WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_post(form_data):
        is_valid = True
        query = "SELECT * FROM posts WHERE post = %(post)s"
        results = connectToMySQL(Post.db).query_db(query, form_data)
        if len(form_data['title']) < 3:
            flash("title must be at least 3 characters long.")
            is_valid = False
        if len(form_data['posting']) < 3:
            flash("Post must be at least 3 characters long.")
            is_valid = False
        return is_valid
