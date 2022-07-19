value = 5


def func():
    global value
    value = 10


print(value)
func()
print(value)
