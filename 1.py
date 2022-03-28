class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
    def __str__(self):
        return f'Прямоугольник (ширина = {self.width}, длина = {self.lenght})'

class Square:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"Квадрат (сторона = {self.a})"


class Circle:
    def __init__(self, r):
        self.radius = r
    def __str__(self):
        return f'Круг (радиус = {self.radius})'

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f'Треугольник (сторона a = {self.a}, сторона b = {self.b}, сторона c = {self.c})'

rectangle = Rectangle(5, 10)
square = Square(6)
circle = Circle(13)
triangle = Triangle(4, 7, 9)

print(rectangle)
print(square)
print(circle)
print(triangle)
