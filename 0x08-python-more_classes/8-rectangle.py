#!/usr/bin/python3
"""Defining class Rectangle"""


class Rectangle:
    """Representing a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructing the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Setter of width"""
        return self.__width

    @property
    def height(self):
        """Setter of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Compute the area of the rectangle"""
        return self.__height*self.__width

    def perimeter(self):
        """Compute the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return the printable representation of the object rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join([self.__width * str(self.print_symbol)
                          for i in range(self.__height)])

    def __repr__(self) -> str:
        """Returns the string representation of the object rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete an instance of the Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_1 if rect_1.area() >= rect_2.area() else rect_2
