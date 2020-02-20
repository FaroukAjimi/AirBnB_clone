#!/usr/bin/python3

""" module that contains basemodel"""

import datetime
import uuid
import json
import models


class BaseModel:
    """ basemodel class"""
    def __init__(self, *args, **kwargs):
        """ init funciton"""
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
            models.storage.new(self)

    def __str__(self):
        """str function"""
        fst = self.__class__.__name__
        snd = self.id
        trd = self.__dict__
        return "[{}] ({}) {}".format(fst, snd, trd)

    def save(self):
        """save function"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """to dict function"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
