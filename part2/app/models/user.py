#!/usr/bin/python3

from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email,is_admin = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # store places related to user

        if (first_name) == None:
            raise ValueError ("empty")

        if len(first_name) > 50:
            raise ValueError ("too long")
        
        if  (last_name) == None:
            raise ValueError ("empty")
        
        if len(last_name) > 50:
            raise ValueError ("too long")

        email == ("enter your email")
        if "@" in email and "." in email:
            print ("valid email")
        else:
            print ("invalid email")

        if email == None:
            raise TypeError ("email is empty")
    def add_place (self, place):
        """Add place to user"""
        self.places.append(place)