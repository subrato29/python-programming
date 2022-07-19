class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def say_hello(self):
        print("Hello", self.name)

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


p1 = Person("Tom")
p2 = Person("David")
p1.say_hello()
p2.say_hello()
p1.set_age(24)
print(p1.age)
print(p1.get_age())


class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked

    def increament(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decreament(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print("The current count is:", self.count)


counter = Counter()
counter2 = Counter()

counter.increament()
counter.increament()
counter.increament()
counter.decreament()

counter.print_count()

counter.toggle_lock()
counter.decreament()
