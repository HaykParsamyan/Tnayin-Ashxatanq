class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def ashxatavardzi_bardzracum(self, tokos):
        avelacum = self.salary * (tokos / 100)
        self.salary += avelacum

    def __repr__(self):
        return str(self.name) +  str(self.age)  + str(self.salary)

employee1 = Employee("Hayk", 16, 50000)
print(employee1)

employee1.ashxatavardzi_bardzracum(10)
print(employee1)
