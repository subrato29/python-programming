class Person:
    # creating constructor
    def __init__(self):  # 'self' contains instance of calling this method
        print("ran")

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Tom", 21)
p2 = Person("Harry", 40)
print(p1.name, p1.age)
print(p2.name, p2.age)
# print (p1)
# print (type (p1))

p1.new = "random"  # created a new attribute
print(p1.new)


class Fruit:
    def __init__(self, name, cals):
        self.name = name
        self.cals = cals


apple = Fruit("Apple", 100)
print(apple.name, apple.cals)

apple.color = "Red"
print(apple.color)
