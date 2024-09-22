class Complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        x_part = self.x * other.x - self.y * other.y
        y_part = self.x * other.y + self.y * other.x
        return Complex(x_part, y_part)

    def __repr__(self):
        return f"Complex({self.x}, {self.y})"

    def __str__(self):
        if self.y >= 0:
            return f"{self.x} + {self.y}i"
        else:
            return f"{self.x} - {-self.y}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
