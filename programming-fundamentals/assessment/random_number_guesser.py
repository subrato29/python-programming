import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
start = input("Enter the start of the range: ")
while not start.isdigit():
    print("Enter a valid number: ")
    start = input("Enter the start of the range: ")

end = input("Enter the end of the range: ")
while not end.isdigit() or int(end) < int(start):
    print("Enter a valid number: ")
    end = input("Enter the end of the range: ")

random_number = random.randint(int(start), int(end))

guess = None
attempt = 0

while guess != random_number:
    guessed_number = input("Continue guessing: ")
    if not guessed_number.isdigit():
        print("Your input is not a valid number.")
        continue

    attempt += 1
    guess = int(guessed_number)

suffix = ""
if attempt > 1:
    suffix = "s"

print("You guess the right number, which is:", guess, "in", attempt, "attempt" + suffix)
