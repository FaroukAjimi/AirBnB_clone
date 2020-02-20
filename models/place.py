#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    descritption = ""
    number_romms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
