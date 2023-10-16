#!/usr/bin/python3
"""Defiasdnes the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represasfenting a place.

    Attrib:
        The Ciasfty id
        The User id
        The name of the place
        The descsafription asof the place
        The numsafber of rooms of the place
        The number of bathrooms of the place
        The maximum numbsaferasf of guests of the place
        The price by niasfght of the place
        The latitusdfde of the plac
        The longitude osaff the place
        list of Amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []