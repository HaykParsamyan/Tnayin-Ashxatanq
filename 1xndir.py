class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self):
        return self.x * self.y

a = Rectangle(2, 3)
print(a.__mul__())