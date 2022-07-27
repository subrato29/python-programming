func = lambda x, y, z=0: x + y + z  # func is actually not the name of the function
print(func(10, 20))

func = lambda x, y, z=0: print(x + y + z)
func(10, 20)
print(func(10, 20))

# sorting
lst = [(1, 2), (-2, -6), (5, 9), (3, 0)]
lst.sort(key=lambda x: x[1])  # soring by first element
print(lst)


# function returning function
def mul(x):
    def mul2(y):
        return x * y

    return mul2


result = mul(5)(2)
print(result)

# another way using lambda
mul = lambda x: lambda y: x * y
result = mul(10)(3)
print(result)
