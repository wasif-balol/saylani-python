class Shape:
    area = 0
    def __init__(self, lenght):
        self.lenght=lenght



class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        a = (self.length * self.length)
        print('The area of a square with a side length of %f is %f' % (self.length, a))


s = Square(2)
s.area()
