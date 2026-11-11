#!/bin/usr/python3

from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
   def __init__(self, title, description, price, latitude, longitude, owner):
      super().__init__()
      self.title = title
      self.description = description
      self.price = price
      self.latitude = latitude
      self.longitude = longitude
      self.owner = owner
      self.reviews = []  
      self.amenities = []

      if (title) == None or title == " ":
         raise ValueError ("empty")
      
      if len(title) > 100:
         raise ValueError ("too long")

      if type(price) not in (int,float):
         raise ValueError ("not good")

      if price <= 0:
         raise ValueError ("the price is negative")

      if type(latitude) not in (int,float):
         raise ValueError ("incorrect")
      
      if not -90 <= latitude <= 90:
         raise ValueError("must be between -90 and 90")

      if type(longitude) not in (int,float):
         raise ValueError ("incorrect")
      
      if  not -180 <= longitude <= 180:
         raise ValueError("must be between -180 and 180")
   @property
   def owner(self):
      return self._owner

   @owner.setter
   def owner(self, value):
      if not isinstance(value, User):
         raise ValueError("Owner must be in the User instance")
      self._owner = value

   def add_amenity(self, amenity):
      """Add an amenity to the place."""
      self.amenities.append(amenity)
   def add_review(self, review):
      """add an review to the place """
      self.reviews.append(review)