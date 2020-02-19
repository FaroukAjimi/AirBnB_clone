#!/usr/bin/python3
import datetime
import uuid
import json
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return(FileStorage.__objects)

    def new(self, obj):
        key = obj.__class__.__name__ +'.'+ obj.id
        FileStorage.__objects[key] = obj
        print()
        print("im in new and objects are")
        print(FileStorage.__objects)
        print()

    def save(self):
        dit = {}
        for key, value in FileStorage.__objects.items():
            dit[key] = value.to_dict()
        strdata = json.dumps(dit)
        with open(self.__file_path, 'w') as file:
            file.write(strdata)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = f.read()
                d = json.loads(data)
                for value in d.values():
                    obj = BaseModel(**value)
                    print()
                    print("in reload and obj is")
                    print(obj)
                    self.new(obj)
        except:
            pass
