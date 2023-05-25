from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from app.models import user
from app.models import post

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = "queenflossy"

class Profile:
    def __init__(self,data):
        self.Pic = data['Pic']
        self.id = data ['id']
        self.First_name = data ['First_name']
        self.Last_name = data ['Last_name']
        self.email = data ['email']
        self.Phone_number = data ['phone_number']
        self.Address = data ['Address']
        self.City = data ['City']
        self.State = data ['State']
        self.Country = data ['Country']
        self.Zip_code = data ['Zip_code']
        self.Education = data ['Education']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']


    @classmethod
    def create_profile(cls, data):
        query = '''
        INSERT INTO profile
        (Pic, First_name, Last_name, email, phone_number, users_id, Address, City, State, Country, Zip_code, Education,  created_at, updated_at)
        VALUES (%(Pic)s, %(First_name)s, %(Last_name)s, %(email)s, %(phone_number)s, %(Address)s, %(City)s, %(State)s, %(Country)s, %(Zip_code)s, %(Education)s, %(Experience)s, %(Additional_details)s, %(users_id)s, NOW(), NOW())
        '''
        return connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_users_profile(cls, user_id):
        query = '''
        SELECT * FROM profile
        WHERE users_id = %(user_id)s
        '''
        results = connectToMySQL(db).query_db(query, user_id)
        print(f"results: {results}")
        if results:
            return cls(results[0])
        else:
            return None
        
    @classmethod
    def get_users_profile_from_post_id(cls, post_id):
        query = '''
        SELECT * FROM posts
        WHERE postt.id = %(post_id)s
        '''
        results = connectToMySQL(db).query_db(query, post_id)
        print(f"results: {results}")
        if results:
            return cls(results[0])
        else:
            return None
        
    @classmethod
    def update_users_profile(cls, user_data):
        query = "UPDATE profile SET Pic = %(Pic)s, First_name = %(First_name)s, Last_name = %(Last_name)s, email = %(email)s, phone_number = %(phone_number)s, Address = %(Address)s, City = %(City)s, Zip_code = %(Zip_code)s, Education = %(Education)s,  updated_at = NOW() WHERE users_id = %(users_id)s;"
        return connectToMySQL(db).query_db(query, user_data)
    

    @staticmethod
    def Profile_validations(form_data):
        if not EMAIL_REGEX.match(form_data['email']):

            flash('Invalid email address.', 'register')
            is_valid = False

        if len(form_data['first_name']) < 2:
            flash('First name must be at least 3 characters.',
                  'register')
            is_valid = False

        if len(form_data['first_name']) < 2:
            flash('First name must be at least 2 characters.',
                  'register')
            is_valid = False

        if len(form_data['last_name']) < 2:
            flash('Last name must be at least 2 characters.',
                  'register')
            is_valid = False
        return is_valid