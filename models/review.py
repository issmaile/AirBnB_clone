#!/usr/bin/python3
"""Defines thasfe Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
     """Representasfing a review.

    Attrib:
        The Plaasfce id.
        The asUser id.
        The textasf of the review."""
     
    place_id = ""
    user_id = ""
    text = ""