lst = [10, 4, 7, 1, 9]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst = [10, 4, 7, 1, 9]
print(sorted(lst))
print(sorted(lst, reverse=True))

tup = [10, 4, 7, 1, 9]
print(sorted(tup))  # return a list

lst = [[10, 1], [8, -2], [15, -8], [7, 4]]
print(sorted(lst))  # default sorted by 1st element


# custom sort: e.g. sort by 2nd element
def sort_by_second_element(item):
    return item[1]


print(sorted(lst, key=sort_by_second_element))
