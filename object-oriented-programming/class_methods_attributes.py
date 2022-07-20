class Car:
    number_of_cars = 0  # class attribute
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.number_of_cars += 1

    @classmethod
    def update_no_of_cars(cls, cars):
        cls.number_of_cars = cars
        print("running")


c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

Car.update_no_of_cars(10)

print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars)


class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)


print(Circle.area(2))
print(Circle.perimeter(4))
print(Circle.get_area_and_perimeter(4))