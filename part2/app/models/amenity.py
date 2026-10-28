#!/usr/bin/python3 

from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

        if not isinstance(name,str) or name == "":
            raise ValueError("name cannot be empty")
        if len(name) > 50:
            raise ValueError("too long")

        
