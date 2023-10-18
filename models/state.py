#!/usr/bin/python3
"""Defs State cls"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state

    Attributes:
        name (str): state name
    """

    name = ""
