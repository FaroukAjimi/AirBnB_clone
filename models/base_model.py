#!/usr/bin/python3

""" module that contains basemodel"""

import datetime
import uuid
import json
from . import storage


class BaseModel:
    """basemodel class"""
    def __init__(self, *args, **kwargs):
        """init funciton"""
        s = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.__class__.__name__ = kwargs['__class__']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'],
                                                         s)
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],
                                                         s)
        else:
            storage.new(self)

    def __str__(self):
        """str function"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """save function"""
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """to dict function"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
