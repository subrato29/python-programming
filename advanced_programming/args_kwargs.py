def sum_items(*args, **kwargs):
    print(args)
    print(sum(args))


sum_items(1, 2, 3, k=2, a=2)
sum_items(1, 2, 3, 4)
sum_items()


def total_items(a, b, c):
    print(a, b, c)
    return a + b + c


kwargs = {
    'a': 5,
    'b': 8,
    'c': 9
}
# args = [4, 5, 7] # works with tuple anf string
# x = total_items (*args)
x = total_items(**kwargs)
print(x)

values = [1, 2, 3, 4, 5]
print(*values)


def test(p1, *args, **kwargs):
    print(p1, args, kwargs)


values = [1, 2, 3, 4, 5]
kwargs = {
    'a': 5,
    'b': 8,
    'c': 9
}
test(6, values, kwargs)
