# Welcome to our Python playground!

lst = [1, 2, 3]
print(lst[0])
print(lst[1])
print(lst[2])

lst = ["Hello", "World"]
lst.append("!")
print(lst[0], lst[1], lst[2])

print(len(lst))

list = [3, 5, 8, 2, "Hello", True]
print(list)

list[1] = 10
print(list)

list.append(20)
print(list)
print(len(list))

str1 = "Subrato"
print(str1[2])

print("-------------------------------")

lst = [1, 2, 3, 2, 1, 1, 1, 5, 1, 9]
print(lst.pop())
print(lst)
print(lst.count(1))
print(lst.index(2))
# print (lst.index(2))
lst.remove(1)
print(lst)
print(2 in lst)

list1 = [1, 2, 3]
list2 = [4, 5]
print(list1 + list2)

list1.extend(list2)
print(list1)

list1 = [1, 2, 3]
list2 = [4, 5]
list2.extend(list1)
print(list2)

# nested list
list1 = [[5, 6, []], [2, 3], [1, 2, 3]]
print(list1[2][1])
