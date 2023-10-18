#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represent an abstactd storage engine

    Attributes:
        __file_path (str): file name to save objs to
        __objects (dict): dict of inited objs
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id . """
        oc_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to json in __file_path"""
        objs = FileStorage.__objects
        obj_dict = {obj: objs[obj].to_dict() for obj in objs.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file in __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
