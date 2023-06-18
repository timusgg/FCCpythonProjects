class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width='+ str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, num):
        self.width = num

    def set_height(self, num):
        self.height= num

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2*(self.height + self.width)
    
    def get_diagonal(self):
        return ((self.height ** 2) + (self.width ** 2)) ** 0.5
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        
        picture = ''

        for _ in range(self.height):
            picture += (self.width * '*') + '\n'
        
        return picture
    
    def get_amount_inside(self, shape : 'Rectangle'):
        areaRectangle = self.get_area()
        shapeArea = shape.get_area()

        numberOfShapes = areaRectangle//shapeArea

        return numberOfShapes 


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def __str__(self):
        return 'Square(side=' + str(self.side) + ')'
    
    def set_side(self, num):
        self.side = num
        super().set_width(num)
        super().set_height(num)       
    
    def set_width(self, num):
        self.side = num
        self.set_side(num)

    def set_height(self, num):
        self.side = num
        self.set_side(num)



rect = Rectangle(10,4)
rect2 = Rectangle(2,4)

print(rect,rect2)
print(rect.get_area())
#rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())
print(rect2.get_picture())
print(rect.get_amount_inside(rect2))


sq = Square(3)
print(sq)
sq.set_side(5)
print(sq)
print(sq.get_area())
print(rect)
print(rect.get_amount_inside(sq))

