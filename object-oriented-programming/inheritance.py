class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print("Hi my name is", self.first_name, self.last_name)


class Employee(Person):
    # Override constructor of Super class
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    # Override the child class
    def say_hello(self):
        print("--------")
        super().say_hello()
        print("My salary is", self.salary)
        print("--------")

    def test(self):
        print("test")


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, dept):
        super().__init__(first_name, last_name, salary)
        self.dept = dept


class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth


emp = Employee("Child", "Coder", 40000)
emp.say_hello()

manager = Manager("Child", "Coder", 40000, "Compuer")
manager.say_hello()

owner = Owner("Owner", "Teacher", 80000)
owner.say_hello()
print(type(owner))
print(isinstance(owner, Person))


# Multiple inheritance
class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()
print(isinstance(c, A))
print(isinstance(c, B))
