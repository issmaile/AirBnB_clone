#!/usr/bin/python3
"""defs Review cls"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review

    Attributes:
        place_id (str): place's id
        user_id (str): user's id
        text (str): review text
    """

    place_id = ""
    user_id = ""
    text = ""
