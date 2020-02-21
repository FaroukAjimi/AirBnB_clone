#!/usr/bin/python3

"""Module That contains FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """class Filestorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all function"""
        return(FileStorage.__objects)

    def new(self, obj):
        """new function"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """save function"""
        dit = {}
        for key, value in FileStorage.__objects.items():
            dit[key] = value.to_dict()
        strdata = json.dumps(dit)
        with open(self.__file_path, 'w') as file:
            file.write(strdata)

    def reload(self):
        """reload function"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for value in data.values():
                    obj = BaseModel(**value)
                    self.new(obj)
        except:
            pass
