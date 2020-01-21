#!/usr/bin/python3
class BaseGeometry:
    """
    Function class BaseGeometry.
    """
    def area(self):
        """
        ublic instance method: def area(self): that raises
        an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: integer validator
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
