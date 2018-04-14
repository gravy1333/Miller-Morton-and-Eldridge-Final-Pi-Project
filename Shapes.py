######################################################################################################################
# Name: Louis Miller
# Date: 4/14/18
# Description: Program to creates shapes out of stars
######################################################################################################################

class Shape(object):
    def __init__(self , w=1, h=1):
        #if width is not greater than 0 set width to one
        if not (w > 0):
            w=1
        #if height is not greater than 0 set height to one
        if not (h > 0):
            h=1
        self.width = w
        self.height = h

    #getter for width
    @property
    def width(self):
        return self._width

    #setter f rwidth
    @width.setter
    def width(self, value):
        #if value is greater than zero set width to value otherwise ignore change
        if (value > 0):
            self._width = value

    #getter for height
    @property
    def height(self):
        return self._height

    #setter for height
    @height.setter
    def height(self, value):
        #if value is greater than zero set height to value otherwise ignore change
        if (value > 0):
            self._height = value

    def __str__(self):
        for i in range(self.height):
            print "* " * self.width
        return ""

class Rectangle(Shape):
    #pass because rectangle will use __init__ and __str__ of shape
    pass

class Square(Shape):
    def __init__(self, w):
        Shape.__init__(self, w, w)

class Triangle(Shape):
    def __init__(self, w):
        Shape.__init__(self, w, w)

    def __str__(self):
        for i in range(self.height):
            print "* " * (self.height - i)
        return ""

class Parallelogram(Shape):
    def __str__(self):
        for i in range(self.height):
            print "  " * (self.height - i - 1)+ "* " * self.width
        return ""

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print r1
s1 = Square(6)
print s1
t1 = Triangle(7)
print t1
p1 = Parallelogram(10, 3)
print p1
r2 = Rectangle(0, 0)
print r2
p1.width = 2
p1.width = -1
p1.height = 2
print p1

