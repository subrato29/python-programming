def func(a=10, b=30):
    return a + b


print(func(50))


def return_multiple_values(x, y):
    return x + 1, y + 1


print(return_multiple_values(3, 9))  # return tuple

x, y = return_multiple_values(12, 15)
print(x, y)


def sum_lists(list1, list2):
    sum1 = sum_list(list1)
    sum2 = sum_list(list2)
    return sum1, sum2


def sum_list(lst):
    total = 0
    for num in lst:
        total += num

    return total


print(sum_lists([1, 2, 3], [10, 11, 12]))
