#!/usr/bin/python3
"""City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city

    Attributes:
        state_id (str): id of state the city is in
        name (str): city name
    """

    state_id = ""
    name = ""
