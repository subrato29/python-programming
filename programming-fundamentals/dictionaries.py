# key value pair

# Welcome to our Python playground!

salaries = {
    "Brad": 10,
    "Lucy": 12,
    "John": 6.5,
}

#print (salaries)
for key in salaries:
    value = salaries[key]
    print (key, value)

for key, value in salaries.items():
    print (key, value)

my_dics = dict() # Creating a brand new dictionary
#OR
my_dics = {}
print (my_dics)

# del salaries["Brad"]
# print (salaries)

#Keys exist
print ("Brad" in salaries)
values = salaries.values();
print (list(values)[1]) #converting in list by list() function

keys = salaries.keys()
print (list(keys)[0])

print (salaries.items()) #return all tupes having key and value
print (len(salaries))

x = {
    1: 11,
    2: 12,
    3: 13
}
x[4] = x.get (4, 0) + 1
print (x)

x[4] = x.get (4, 0) + 1 #equivalent to getOrDefault() function in Java
print (x)

# frquemcy of characters in a String
string = "hello world"
dics = {}

for ch in string:
    dics[ch] = dics.get (ch, 0) + 1

print (dics)