#!/usr/bin/python3
class Student:
    """
    Class for define a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes for student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that return a dictionary
        Depending the attributes
        """
        if type(attrs) is not list:
            return self.__dict__
        dict = {}

        for i in attrs:
            validate = getattr(self, i, None)
            if validate is not None:
                dict[i] = validate
        return dict
