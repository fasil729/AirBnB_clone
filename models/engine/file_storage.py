#!/usr/bin/python3
"""module consists class for serilazition and deserilaztion"""
from json import dump, load, dumps
from os.path import exists
from models.base_model import  BaseModel


name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage:
    """serializes instances to a JSON file and
        deserializes JSON file to instances
        """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary object"""
        return __class__.__objects

    def new(self, obj):
        """sets the obj to with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fil = open(__class__.__file_path, 'w', encoding='utf-8')
        dic_to_json = {}
        for obj, val in __class__.__objects.items():
            dic_to_json[obj] = val.to_dict()
        dump(dic_to_json, fil)
        fil.close()

    def reload(self):
        """ if (__file_path) exists deserializes JSON file to __objects
            elif , do nothing. If the file not exist,
        """
        dic_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dic_obj = load(fil)
                for key, value in dic_obj.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass
