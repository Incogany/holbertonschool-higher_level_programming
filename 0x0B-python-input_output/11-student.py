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

    def to_json(self):
        """
        Method that return a dictionary
        """
        return self.__dict__
