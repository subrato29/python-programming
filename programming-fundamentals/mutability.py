# mutable(changeable) data type
list()
set()
dict()

# immutable
tuple()

x = []
y = []
print(x is y)  # use 'is' to validate whther 2 objects are same or not
print(id(x), id(y))

y = x
print(x is y)
print(id(x), id(y))

x = 1
y = 1
print(x is y)
print(id(x), id(y))

lst = [1, 2, 3]
x = {
    1: lst
}
lst.append(100)
print(x)

x = 2
d = {1: x}
print(d)

x = 3
print(d)

# immutable
tuple()
a = [1, 2]
b = [3, 4]
tup = (a, b)

a.append(100)

print(tup)  # We can store mutable objects inside immutable datatype and vice versa
