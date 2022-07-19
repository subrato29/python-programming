lst = [1, 2, 3, 4]
try:
    print(int("hello"))
    lst[2] = 100;
except Exception as e:
    print("Exception is:", e)
finally:
    print(lst)
    print("Done!")

# raising own exception
num = 10
if type(num) == int:
    print("This is valid number")
else:
    raise Exception("This is not a valid number")
