class Rect():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def rectangle_area(self):
        return self.lenght * self.width

figure = Rect(5, 7)
print(figure.rectangle_area())
