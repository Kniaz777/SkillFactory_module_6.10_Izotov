class Rectangle:
    def __init__(self,x,y,widht,height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height

    def __str__(self):
        return 'Прямоугольник({}, {}, {}, {})'.format(self.x, self.y, self.widht, self.height)

figure = Rectangle(1, 4, 32, 58)
print(figure)
print()