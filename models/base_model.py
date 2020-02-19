#!/usr/bin/python3
import datetime
import uuid
import json
from . import storage
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.key = value
            self.__class__.__name__ = kwargs['__class__']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            print("\nim in init kwargs\n")
        else:
            self.id = str(uuid.uuid4())
            self.created_at =  datetime.datetime.now()
            self.updated_at  = datetime.datetime.now()
            storage.new(self)
            print("I'm in init base model new instance")
            
    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[key] = value
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)
