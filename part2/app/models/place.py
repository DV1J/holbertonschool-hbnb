#!/bin/usr/python3

from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

        if (title) == None:
            raise ValueError ("empty")
        if len(title) > 100:
         raise ValueError ("too long")
        if type(price) not in (int,float):
           raise ValueError ("not good")
        if price < 0:
           raise ValueError ("the price is negative")
        if type(latitude) not in (int,float):
           raise ValueError ("incorrect")
        if latitude is not -90 <= latitude >= 90:
           raise ValueError("must be between -90 and 90")
        

           
        

        
