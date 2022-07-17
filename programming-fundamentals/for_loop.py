# Welcome to our Python playground!

names = ["Tim", "Clement", "Antoine"]
for name in names:
    print(f"Name in list: {name}")


for i in range(1, 10, 2):
    print(f"i = {i}")

for i in range (1, 10):
    print (i)

for i in range (10):
    print (i)

list = [1, 2, 3, 4, 5, True, False, 6]
for element in list:
    print (element)

for i, element in enumerate(list):
    print (i, element)

for element in list:
    if element == 4:
        break;
    print (element)

for element in list:
    if element == 4:
        continue;
    print (element)

tuple = (1, 2, 3, 4, 5, True, False, 6)
for i in range (len(tuple)):
    print (tuple[i])

for element in tuple:
    print (element);

for i, element in enumerate(tuple):
    print (i, element)

target = 16;
for element in tuple:
    if element == target:
        print ("found")
        break
else:
    print ("not found")

string = "Subrato"
for ch in string:
    print (ch)

for i, ch in enumerate(string):
    print (i, ch)

for i in range (10):
    for j in range (10):
        print (i, j)

for i in range (10):
    pass