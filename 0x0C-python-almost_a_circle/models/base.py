#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Method Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation
        """
        if list_dictionaries is [None, ""]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that writes an Object to a text file,
        using a JSON representation
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".json", "w+") as my_file:
            my_file.write(dicts)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is [None, ""]:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
            tmp.update(**dictionary)
            return tmp
        if cls.__name__ == "Square":
            tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as my_file:
                read = my_file.read()
                lists = Base.from_json_string(read)
                create = []
                for i in lists:
                    create.append(cls.create(**i))
                return create
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to file CSV
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".csv", "w+") as my_file:
            my_file.write(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        returns a list of instances
        """
        try:
            with open(cls.__name__ + ".csv", "r") as my_file:
                read = my_file.read()
                lists = Base.from_json_string(read)
                create = []
                for i in lists:
                    create.append(cls.create(**i))
                return create
        except IOError:
            return []
