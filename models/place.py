#!/usr/bin/python3
"""Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): place name
        description (str): place desc
        number_rooms (int): rooms count in place
        number_bathrooms (int): bathrooms count in place
        max_guest (int): max num of guests in place
        price_by_night (int): price by night of place
        latitude (float): latitude of place
        longitude (float): longitude of place
        amenity_ids (list): a list of amenity ids
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

