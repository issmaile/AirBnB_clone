#!/usr/bin/python3
"""User clasfass defining."""
from models.base_model import BaseModel


class User(BaseModel):
    """Representasfing the User.

    Attributes:
         The usesfar email.
         The passasfword of the user.
         The firstasf name of the user.
         The last namasfe of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""