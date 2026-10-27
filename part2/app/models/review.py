#!/usr/bin/python3

from app.models.base_model import BaseModel

class review(BaseModel):
    def __init__(self, text, rating, place, user):
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

        