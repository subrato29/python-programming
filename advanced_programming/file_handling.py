file = open ("file.txt", "r")
print(file.read())
file.close()

# read
with open("file.txt", "r") as file:
    # print(file.read())
    line1 = file.readlines()[2]
    print(line1.strip())

# write
with open("file1.txt", "w") as file:
    file.write("This is a new file")

# reading and writing
with open("file1.txt", "r+") as file:
    score = file.read()
    new_score = int(score) + 1
    file.seek(0)
    file.write(str(new_score))

# iterating through the lines
with open("file1.txt", "r+") as file:
    for i, line in enumerate (file):
        print(line, end="")
        if i == 2:
            break

# reading certain characters in line
with open("file1.txt", "r+") as file:
    print(file.read(7))

