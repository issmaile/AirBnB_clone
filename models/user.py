#!/usr/bin/python3
"""Defs User cls"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): User email
        password (str): User pwd
        first_name (str): User first name
        last_name (str): User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
