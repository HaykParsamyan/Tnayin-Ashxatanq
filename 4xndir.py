from xmlrpc.client import boolean


class Circle:
    def __init__(self, r):
        self.r = r
    def __gt__(self, other):
        return self.r > other.r
    def __repr__(self):
        return boolean

circle1 = Circle(5)
circle2 = Circle(3)

print(circle1 > circle2)
print(circle2 > circle1)
