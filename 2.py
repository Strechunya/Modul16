class Rectangle():
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
    def rectangle_area(self):
        return self.width*self.lenght

newRectangle = Rectangle(10,12)
print ("Площадь прямоугольника =", newRectangle.rectangle_area())
