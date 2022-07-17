# Welcome to our Python playground!
# Tuples also works like String and List. The difference is
# List is mutable and Tuple is immutable

t1 = (1, 2)
t2 = (3, 4, 5, 3)

print(len(t1), len(t2))

print(t1.count(3))
print(t2.count(3))

print(t1.index(2))

print(t1[0])

print (t1 + t2)
print (t1 * 2)
print ([1] * 5)

x = 1, 2, 3, 4
print (x)

x = (1) #tuple with a single element considered as an int.
print (x)

# To make it tuple with single element, write like this (1, )
x = (1, )
print (x)