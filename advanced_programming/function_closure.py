def outer(x, y):
    def nested():
        return x + y

    return nested


value = outer(1, 2)()
print(value)


def foo(x):
    print(x)


print(type(foo))


def call_func(func, x):  # pass function as parameter
    func(x)


call_func(foo, 10)


def outer(x):  # enclosing function
    def inner(y):  # nested function
        print(x + y)

    return inner


x = outer(8)(5)
print(x)


def outer(x):
    def inner():
        print(x)

    return inner


func = outer(5)
func()
outer(10)()


class Collection:
    def __init__(self):
        self.lst = []

    def add_value(self, value):
        self.lst.append(value)
        return self.lst


# equivalent to Collection class
def collection():
    lst = []

    def inner(value):
        lst.append(value)
        return lst

    return inner


add_value = collection()
print(add_value(1))
print(add_value(2))
print(add_value(3))


def counter(start):
    count = start

    def increment(val):
        nonlocal count
        count += val
        return count

    return increment


count = counter(2)
print(count(1))
print(count(1))
print(count(1))
