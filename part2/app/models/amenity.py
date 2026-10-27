#!/usr/bin/python3 

from app.models.base_model import BaseModel

class amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
