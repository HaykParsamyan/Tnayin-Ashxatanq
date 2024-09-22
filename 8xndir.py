class Erankyun:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ka_chka(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def paragic(self):
        return self.ka_chka() * (self.a + self.b + self.c)
c
    def makeres(self):
        s = self.paragic() / 2
        return self.ka_chka() * ((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5)

    def __repr__(self):
        return f"Erankyun(a={self.a}, b={self.b}, c={self.c})"

x = Erankyun(3, 4, 5)
print(x)
print("paragic:", x.paragic())
print("makeres:", x.makeres())

