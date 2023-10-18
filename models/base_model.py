#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent BaseModel of HBnB project"""

    def __init__(self, *args, **kwargs):
        """Init a new BaseModel

        Args:
            *args (any): unused
            **kwargs (dict): key/value pairs of attrs
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if keu == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Set updated_at to be current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dict of the BaseModel instance

        Includes the key/value pair __class__ representing
        the object's class name
        """
        retdict = self.__dict__.copy()
        retdict["__class__"] = self.__class__.__name__
        retdict["created_at"] = self.created_at.isoformat()
        retdict["updated_at"] = self.updated_at.isoformat()
        return retdict

    def __str__(self):
        """Return the print/str representatoin of the BaseModel instanceee"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
