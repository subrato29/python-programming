x = set() #empty set
y = {} # for an empty set use set(). If you use {} it will be a dictionary
z = [] #empty list

print (type (x))
print (type (y))
print (type (z))

set = {1, 2, 3, 2, 3, 3}
print (set)

set.add (4)
print (set)

set.remove (4)
print (set)

set.clear()
print (set)

set = {1, 2, 3, 2, 3, 3}
print (len(set))

set.add ("3")
print (set)

#print (set.add ([10, 34])) #you can't add a list,dictionary, set into a set
#set.add ({3, 4})
set.add ((76, 45)) # you can tuple inside a set
print (set)
print (len(set))

print (1 in set)

x = {1, 2}
y = {2, 3}
print (x.union (y))
print (x | y)
print (x.intersection(y))
print (x - y)

x.update(y)
print (x)

y.update(x)
print (y)

x = {1, 2}
y = {1, 2, 3, 4}
print (x < y) #subset
print (y > x) #superset

# conversion list to set
list1 = [1, 2, 2, 3, 4, 4, 5, 4, 2]
set_x = set(list1)
print(set_x)

# conversion of set into list
list2 = list(set_x)
print(list2)