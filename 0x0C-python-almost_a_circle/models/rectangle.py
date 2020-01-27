#!/usr/bin/python3
""" Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Method recover the value Width Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method Evaluate the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Method recover the value Width Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method Evaluate the value of width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method recover the value Width Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method Evaluate the value of width"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method recover the value Width Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method Evaluate the value of width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        method the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        print the rectangle
        """
        display = ""
        tmp = self.__x
        for i in range(0, self.__height):
            if self.__y is not 0:
                display += self.__y * "\n"
                self.__y = 0
            for j in range(0, self.__width):
                if self.__x is not 0:
                    display += self.__x * " "
                    self.__x = 0
                display += "#"
            display += "\n"
            self.__x = tmp
        display = display[:-1]
        print("{}".format(display))

    def __str__(self):
        """
        Print an Unofficial string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        *Args: This type of argument is called a “no-keyword argument”
        - Argument order is super important.
        **kwargs can be thought of as a double pointer to a dictionary:
        key/value
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        dic = {}
        dic['x'] = self.x
        dic['y'] = self.y
        dic['id'] = self.id
        dic['height'] = self.height
        dic['width'] = self.width
        return dic
