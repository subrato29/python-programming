# Welcome to our Python playground!

name = "Tim"
print(name.upper())
print(name.lower())

greeting = "Hello " + name
print(greeting)
print(len(greeting))

if name in greeting:
    print("The name is contained in the greeting!")

print(f"The first character of the name is {name[0]}")

name = "Subrbbbato"
print (name.count('b'))
print (name.find ('b'))
print (name.upper ())
print (name.lower ())
print ('r' in name)
print (name.__contains__('r'))

name = "abcd"
print (name.capitalize())

string = "15"
print (string.isdigit())

string = "15.8"
print (string.isdigit())

num = "59"
if num.isdigit ():
    print ("This is a digit")
    print (int(num) + 5)
else:
    print ("This is a string")

string = "I am learning Python"
list = string.split ()
print (list)

string = "I,am,learning,Python"
list = string.split (",")
print (list)
print (string.replace (",", "|"))

string = "World"
print (f"Hello {string}, beautiful {string} {6 + 4}")

print (string * 4)

string = """Hello this is Subrato
I am new to Python
I am enjoying
Python
"""
print (string)

list1 = ["A", "B", "C"]
print ("".join (list1))
print ("|".join (list1))