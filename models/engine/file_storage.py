#!/usr/bin/python3
""" FileStorage class serializes instances to a JSON
file and deserializes JSON file to instances """
import json
import os
from .. import base_model


class FileStorage():
    """File Storage class that serializes and deserializes
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            Get all object members

            Returns: __objects (dict)
        """
        return self.__objects

    def new(self, obj):
        """
            Sets private class attribute __object to given
            object (obj) with key "classname.obj[id]"
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
            Serializes object to JSON and save to file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            _obj = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(_obj, f)

    def reload(self):
        """
            Deserializes JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                json_dict = json.load(f)
                for obj in json_dict.values():
                    class_n = obj['__class__']
                    del obj['__class__']
                    self.new(eval(f'base_model.{class_n}')(**obj))
