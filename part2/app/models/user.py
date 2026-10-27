#!/usr/bin/python3

from app.models.base_model import BaseModel

class user(BaseModel):
    def __init__(self_id, first_name, last_name, email,is_admin = False):
        super().__init__()
        self_id.first_name = first_name
        self_id.last_name = last_name
        self_id.email = email
        self_id.is_admin = is_admin

        if len(first_name) > 50:
            raise ValueError ("too long")
        
        if len(last_name) > 50:
            raise ValueError ("too long")
        