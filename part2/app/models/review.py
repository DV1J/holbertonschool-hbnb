#!/usr/bin/python3

from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User

class review(BaseModel):
    def __init__(self, text, rating, place, user):
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

        if not isinstance (text,str):
            raise ValueError("review is empty")
        if type(rating) is not int:
            raise ValueError("rating must be integer")
        if  not 1 <= rating <= 5:
            raise ValueError("rating must be between 1 and 5")
        if not isinstance (place, Place):
            raise ValueError("place must be a place instance")
        if not isinstance (user, User):
            raise ValueError("place must be a place instance")
        
        